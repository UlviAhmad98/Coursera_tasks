dormitory={
    'nmbr':'5',
    'tenants':
    [
        {'name':'Ulvi Ahmadov', 'flat':'307B'},
        {'name':'Javid Aslanli','flat':'307B'},
        {'name':'Junaid Farrukh','flat':'307A'},
        {'name':'Kseniya Akimova','flat':'407B'},
        {'name':'Dariana Khistieva', 'flat': '305B'}
    ]
}

for tenant in dormitory['tenants']:
    print(tenant['name'])
   