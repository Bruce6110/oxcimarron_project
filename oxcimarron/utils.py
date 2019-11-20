import operator
import datetime
from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size
    #10485760
    
    
    if filesize > 3*(2**20):
        raise ValidationError(
            "The maximum file size that can be uploaded is "+str(3*(2**20)))
    else:
        return value



class Utils:

    @staticmethod
    

    @staticmethod
    def printSettings(settings):
        print("\n\n\n\n\n============= SETTINGS ==============")
        print("\nCurrent date/time: ", datetime.datetime.now().time(), "\n")
        for name in dir(settings):
            if name == "__dict__":
                continue  # skip the dict as it's redundant
            print(name+"   =   ", getattr(settings, name))

        print("\n=======================================\n\n\n")

    @staticmethod
    def printDictionary(x, label):

        print("\n------STARTED ITERATING " +
              label.upper()+"-----------------------\n")
        for field, possible_values in x.items():
            print(field, Utils.getAttributeReport(possible_values))

        print("\n------FINISHED ITERATING " +
              label.upper()+"-----------------------\n")

        # print("\n\nLocal Variables: \n")
        # for k in globals().copy().keys():
        #     if k == '__builtins__':
        #         continue
        #     print(k, globals().get(k), "\n")

    @staticmethod
    def getAttributeReport(object):
        report = "\n\n\nATTRIBUTES OF OBJECT '" + \
            str(object)+"\n"+("-"*100)+"\n\n"
        attributes = dir(object)
        attributes.sort()
        counter = 0

        outputList = []
        for item_name in attributes:

            counter += 1

            if(item_name == "objects"):
                continue  # for some reason the 'objects' object causes exception

            result = ""
            try:
                result = getattr(object, item_name)
            except Exception:
                result="*** EXCEPTION: couldn't get result for "+str(object)+", "+item_name                
                continue

            

            
            object_type = str(type(result))

            value = ""
            if 'wrapper' in type(result).__name__:
                continue
            if isinstance(result, list):
                for y in result:
                    #print("list detected ",y)
                    value = value + "\t\t"+str(y)+"\n"
            elif isinstance(result, dict):
                if len(result) > 0:
                    value = value+"\n"
                for key, val in result.copy().items():
                    value = value+"\t\t\t"+str(key)+" : "+str(val)+"\n"
                value = value+"\n"
            else:
                value = value+"\t   =   \t     " + str(result)

            row = [object_type, item_name, value]
            outputList.append(row)

        outputListSorted = sorted(outputList, key=operator.itemgetter(0, 1))

        for listItem in outputListSorted:
            report = report+listItem[0]+"\t"+listItem[1]+"\t"+listItem[2]+"\n"

        return report
