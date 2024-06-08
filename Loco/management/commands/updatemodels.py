from django.core.management.base import BaseCommand
from .ScrapedData import data

class Command(BaseCommand):
    help = "Please refer to the github repository"

    def handle(self,*args, **kwargs):
        data.getBroadElectric()
        self.stdout.write("Imported Electric-Broad Locomotives")
        data.getMeterElectric()
        self.stdout.write("Imported Electric-Meter Locomotives")
        data.getBroadDiesel()
        self.stdout.write("Imported Deisel-Broad Locomotives")
        data.getMeterDiesel()
        self.stdout.write("Imported Deisel-Meter Locomotives")
        data.getNarrowDiesel()
        self.stdout.write("Imported Deisel-Narrow Locomotives")
        data.getNarrowerDiesel()
        self.stdout.write("Imported Deisel-Narrower Locomotives")
        data.getDualBroad()
        self.stdout.write("Imported Dual-Broad Locomotives")
    
        self.stdout.write("Database Updated. No issues detected")
