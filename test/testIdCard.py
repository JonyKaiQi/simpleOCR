#!/usr/bin/env python3

from bin.AccessToken.AccessToken import AccessToken
from bin.Idcard.Idcard import Idcard
from bin.tool.ExcelTools import  simple_general

book_name_xls = 'idCard.xls'

sheet_name_xls = '身份证结果'

value_title = [["序号", "身份证号", "姓名", "地址", "生日", "性别", "民族", "签发机关", "有效期开始开始", "有效期限结束"], ]


def opt_valueScuess(modelFront, modelBack, index):
    if type(modelFront).__name__ == 'dict' and  type(modelBack).__name__ == 'dict' :
        # if 'words_result' in modelFront.keys() and 'words_result' in modelBack.keys():
            address = ''
            if'words_result' in modelFront.keys() and '住址' in modelFront["words_result"].keys():
                address = modelFront["words_result"]["住址"]["words"]
            both = ''
            if'words_result' in modelFront.keys() and '出生' in modelFront["words_result"].keys():
                both = modelFront["words_result"]["出生"]["words"]
            name = ''
            if'words_result' in modelFront.keys() and '姓名' in modelFront["words_result"].keys():
                name = modelFront["words_result"]["姓名"]["words"]
            cardNo = ''
            if'words_result' in modelFront.keys() and '公民身份号码' in modelFront["words_result"].keys():
                cardNo = modelFront["words_result"]["公民身份号码"]["words"]
            sex = ''
            if'words_result' in modelFront.keys() and '性别' in modelFront["words_result"].keys():
                sex = modelFront["words_result"]["性别"]["words"]
            nation = ''
            if'words_result' in modelFront.keys() and '民族' in modelFront["words_result"].keys():
                nation = modelFront["words_result"]["民族"]["words"]
            exitDate = ''
            if'words_result' in modelBack.keys() and '失效日期' in modelBack["words_result"].keys():
                exitDate = modelBack["words_result"]["失效日期"]["words"]
            sign = ''
            if'words_result' in modelBack.keys() and '签发机关' in modelBack["words_result"].keys():
                sign = modelBack["words_result"]["签发机关"]["words"]
            signDate = ''
            if'words_result' in modelBack.keys() and '签发日期' in modelBack["words_result"].keys():
                signDate = modelBack["words_result"]["签发日期"]["words"],
            model = [str(index), cardNo, name, address, both, sex, nation, sign, signDate, exitDate]
            return model
    else:
        model = [str(index), '']
        return model;

if __name__ == '__main__':
    image = 'generalBasic.png'  # 普通图片
    IDCARD_IMAGE = ['1030_idcard_back.png', '1030_idcard_face.png']  # 身份证识别测试照片 0正面，1反面
    url = 'https://user-gold-cdn.xitu.io/2018/6/27/16441ddfa026968b?w=513&h=389&f=png&s=2155'  # 网络图片

    # 测试获取AccessToken
    testAccessToken = AccessToken()
    # 身份证识别, 正面
    # front：身份证含照片的一面；back：身份证带国徽的一面
    value = []
    for k in range(850,870):
        IDCARD_IMAGE[0]= str(k)+"_idcard_face.png"
        testIdcard = Idcard(image=IDCARD_IMAGE[0], id_card_side='front')
        modelFront = testIdcard.postIdcard()
        print('身份证识别正面：', modelFront)

        # 身份证识别, 反面
        # front：身份证含照片的一面；back：身份证带国徽的一面
        IDCARD_IMAGE[1] = str(k) + "_idcard_back.png"
        testIdcard1 = Idcard(image=IDCARD_IMAGE[1], id_card_side='back')
        modelBack = testIdcard1.postIdcard()
        print('身份证识别反面：',modelBack)
        value.append(opt_valueScuess(modelFront, modelBack, k))

    print(value)
    simple_general(book_name_xls,sheet_name_xls,value_title,value)

