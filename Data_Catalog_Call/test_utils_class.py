from utils_Class import ODSDataCatalog

# setting security: using Resource Principal
ads.set_auth(auth='resource_principal')

# define the data catalog object the user wants to access, in this format: Catalog ID, Asset Key, Namespace ID
catalog = ODSDataCatalog("ocid1.datacatalog.oc1.eu-frankfurt-1.aaaaaaaap6lel4hqckltn7fvjnux42jepzohdktkceywlyrnnrwgolbupzhq"
                         , "0e4d60d9-d5b5-467f-89bb-22db63a3ee18", "6adf4ea3-67d5-44a3-b4f7-19fbf303d539")

# define the file the user wants to analyze
file_name = "cs-training-nonull.csv"
bucket = "credit_scoring"

key_name = catalog.get_key_from_name(file_name)
hash_value = catalog.get_hash_from_catalog(name=file_name)
md5_comput = catalog.get_hash_from_file(file_name, bucket)
version_number = catalog.get_version_from_catalog(name=file_name)
assert(key_name == '680cdc2c-febb-45a7-b0f0-39301a296564')
assert(hash_value == '0b43cf47b2a1b336991f2d43b16d0c1e' )
assert(md5_comput == '0b43cf47b2a1b336991f2d43b16d0c1e' )
assert(version_number == 'v1.1')