from products.bulk_insert import bulk_test_data
from django.core.management import BaseCommand, CommandError
class Command(BaseCommand):
        args = '<shop_id shop_id shop_id ...>' 
        
        def handle(self, *args, **options): 
            try:
                bulk_test_data()
            except Exception as e:
                raise CommandError(str(e))
            
            self.stdout.write('Successfully closed command' )

