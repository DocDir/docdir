from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
import requests
from plans.models import Insurer

class Command(BaseCommand):
    help = 'Crawls Socrata and inserts data into db'

    def handle(self, *args, **options):
        self.stdout.write("Pulling Socrata Records")
        SocrataRecordHandler.populate_db(25, 5)
        self.stdout.write("Finished writing Socrata Records")
        
class SocrataRecordHandler:

    base_url = 'https://data.healthcare.gov/resource/qhp-landscape-individual-market-medical.json?'
    key = 'I2NNV2INCPX0CBFQuNQ7H3NPx'
    LIMIT = 50000
    
    # TODO - take this part out and let command handle the creation of the objects
    @classmethod
    def load_json_to_db(self, json):
        for item in json:
            plan = Insurer(name=item['issuer_name'])
            try:
                plan.save()
            except IntegrityError:
                print("Not accepting duplicate: %s" % plan)
        
    @classmethod
    def get_num_records(cls):
        """Get number of all records in db """
        r = cls.query_socratic("$select=count(1)")
        return int(r.json()[0]['count_1'])

    @classmethod
    def populate_db(cls, num = None, simul_limit = None):
        # if limit specified, do this in chunks, else free for all
        # then load json to django
        count = 0
        inc = simul_limit if simul_limit else cls.LIMIT # num to pull simultaneously
        num = num if num else cls.get_num_records() # max num of records to pull
        while count < num:
            r = cls.query_socrata_subset(inc, count)
            cls.load_json_to_db(r.json())
            count += inc

    @classmethod
    def query_socrata_subset(cls, limit = None, offset = None, state = None):
        """Get subset of all records """
        state_field = "state=%s" % state if state else None
        limit_field = "$limit=%s" % limit if limit else None
        offset_field = "$offset=%s&$order=:id" % offset if offset else None
        field_string = '&'.join([x for x in (state_field, limit_field, offset_field) if x])
        return cls.query_socrata(field_string)
        
    @classmethod
    def query_socrata(cls, query_string):
        """Ask socrata for records """
        r = requests.get(cls.base_url + query_string, headers = {'X-App-Token': cls.key})
        if r.status_code != 200:
            raise RuntimeError("Socratic Query had non-200 response: %s\nJSON: %s" % (r.status_code, r.json()))
        return r
