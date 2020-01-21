import zeep

my_client = zeep.Client('http://apps.charitycommission.gov.uk/Showcharity/API/SearchCharitiesV1/SearchCharitiesV1.asmx?wsdl')
key = open('keyfile', 'r').read().splitlines()[0]
api_search_criteria = my_client.get_type('ns0:APISearchCriteria')()
api_search_criteria.SearchFor = 'OnlyRegisterCharities'
api_search_criteria.Keyword = 'MatchAnyWords'
api_search_criteria.SearchIn = 'All'
api_search_criteria.WhereOperates = {'EnglandAndWales': 'OnlySpecific', 'Specific': 'B-19'}
api_search_criteria.RegistrationDateFrom_Day = 0
api_search_criteria.RegistrationDateFrom_Month = 0
api_search_criteria.RegistrationDateFrom_Year = 0
api_search_criteria.RegistrationDateTo_Day = 0
api_search_criteria.RegistrationDateTo_Month = 0
api_search_criteria.RegistrationDateTo_Year = 0
api_search_criteria.RemovedDateFrom_Day = 0
api_search_criteria.RemovedDateFrom_Month = 0
api_search_criteria.RemovedDateFrom_Year = 0
api_search_criteria.RemovedDateTo_Day = 0
api_search_criteria.RemovedDateTo_Month = 0
api_search_criteria.RemovedDateTo_Year = 0
api_search_criteria.RegistrationDateFromIsSpecified = False
api_search_criteria.RegistrationDateToIsSpecified = False
api_search_criteria.RemovedDateFromIsSpecified = False
api_search_criteria.RemovedDateToIsSpecified = False
api_search_criteria.IncomeRangeFrom = 1
api_search_criteria.IncomeRangeTo = 100000
# api_search_criteria.SearchKeyword = 'homelessness'
my_result = my_client.service.GetCharities(key, api_search_criteria)
"""
print(f"Sample getCharity Entry:\n{my_result[0]}")
my_specific_result = my_client.service.GetCharityByRegisteredCharityNumber(key, my_result[0]['RegisteredCharityNumber'])
print(f"Sample get individual charity result:\n{my_specific_result}")
hackney_flattened = []
"""
print(len(my_result))

