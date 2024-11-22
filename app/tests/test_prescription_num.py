from app import app
import utility, pytest, json

# to change status and move to old list
def test_update_prescriptions_3():
    # client = utility.get_client_by_phone("(444)-656-6565")
    # acts = utility.get_active_prescripts(client)
    # olds = utility.get_old_prescripts(client)
    
    # p = acts.pop()
    # p[4] = "5"
    # olds.append(p)
    
    # response = app.test_client().post('/update_list', json={
    #     'id': "(444)-656-6565",
    #     'active': acts, 
    #     'old': olds
    # }, )
    
    response =  app.test_client().get('/clients')
    
    print("(444)-656-6565" in response.data)


# to change status and move to new list 
# def test_update_prescriptions_4():
#     client = utility.get_client_by_phone("(444)-656-6565")
#     acts = utility.get_active_prescripts(client)
#     olds = utility.get_old_prescripts(client)
    
#     p = olds.pop()
#     p[4] = "2"
#     acts.append(p)
    
#     utility.update_prescriptions("(444)-656-6565", acts, olds)
    
#     acts_after = utility.get_active_prescripts(client)
#     olds_after = utility.get_old_prescripts(client)
    
#     assert acts == acts_after
#     assert olds == olds_after