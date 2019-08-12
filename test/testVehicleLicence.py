
from bin.AccessToken.AccessToken import AccessToken
from bin.VehicleLicense.VehicleLicense import VehicleLicense
from bin.tool.ExcelTools import simple_general
book_name_xls = 'vehicleLicenceFace.xls'

sheet_name_xls = '行驶证结果'

value_title = [["图片序号", "车牌号", "车辆类型", "所有人", "住址", "使用性质", "车架号", "车辆识别代号", "发动机号码", "注册日期", "发证日期"], ]

results = []

def opt_value(result, sort):
    if type(result).__name__ == 'dict':
        if'words_result' in result.keys() :
            results = result["words_result"]
            plateNum = ""
            if '号牌号码' in results.keys():
                plateNum = results["号牌号码"]["words"]
            vehType = ""
            if '车辆类型' in results.keys():
                vehType = results["车辆类型"]["words"]
            owner = ""
            if '所有人' in results.keys():
                owner = results["所有人"]["words"]
            addres = ""
            if '住址' in results.keys():
                addres = results["住址"]["words"]
            property = ""
            if '使用性质' in results.keys():
                property = results["使用性质"]["words"]
            modelType = ""
            if '品牌型号' in results.keys():
                modelType = results["品牌型号"]["words"]
            vehNo = ""
            if '车辆识别代号' in results.keys():
                vehNo = results["车辆识别代号"]["words"]
            engineNo = ""
            if '发动机号码' in results.keys():
                engineNo = results["发动机号码"]["words"]
            issueDate = ""
            if '发证日期' in results.keys():
                issueDate = results["发证日期"]["words"]
            registerDate = ""
            if '注册日期' in results.keys():
                registerDate = results["注册日期"]["words"]
            elif '注册登记日期' in results.keys():
                registerDate = results["注册登记日期"]["words"]
            model = [str(sort), plateNum, vehType, owner, addres, property, modelType, vehNo, engineNo, registerDate, issueDate]
            return model
    else:
        model = [str(sort), "", "", "", "", "", "", "", "", "",""]
        return  model



if __name__ == '__main__':

    # XSZ = '231_vehicle_face.png'  # 行驶证识别
    # 测试获取AccessToken
    testAccessToken = AccessToken()
    # # print('Access_token:', testAccessToken.getToken())
    result = []
    for k in range(1503,1619):
        XSZ = str(k) +'_vehicle_face.png'
        testVehicleLicense = VehicleLicense(image=XSZ)
        result = testVehicleLicense.postVehicleLicense()
        print(result)
        model = opt_value(result, k)
        results.append(model)

    # Excel 生成
    simple_general(book_name_xls,sheet_name_xls,value_title,results)

