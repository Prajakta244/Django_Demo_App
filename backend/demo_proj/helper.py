from .db_connection import counter_collection

def get_employee_id():
    res = counter_collection.find_one_and_update(
        {'_id':'employee_id'},
        {'$inc':{'seq':1}},
        upsert=True,
        return_document=True
    )
    return res['seq']