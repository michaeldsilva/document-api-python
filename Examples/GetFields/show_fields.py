############################################################
# Step 1)  Use Datasource object from the Document API
############################################################
from tableaudocumentapi import Datasource

############################################################
# Step 2)  Open the .tds we want to inspect
############################################################
sourceTDS = Datasource.from_file('World.tds')

############################################################
# Step 3)  Print out all of the fields and what type they are
############################################################
print('----------------------------------------------------------')
print('--- {} total fields in this datasource'.format(len(sourceTDS.fields)))
print('----------------------------------------------------------')
for count, field in enumerate(sourceTDS.fields.values()):
    print('{:>4}: {} is a {}'.format(count+1, field.name, field.datatype))
    blank_line = False
    if field.calculation:
        print('      the formula is {}'.format(field.calculation))
        blank_line = True
    if field.aggregation:
        print('      the default aggregation is {}'.format(field.aggregation))
        blank_line = True

    if blank_line:
        print('')
print('----------------------------------------------------------')
