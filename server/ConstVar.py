import os
CurrentPath = os.path.dirname(__file__)
DB_PATH = CurrentPath + '/CoronaBotDB'
MaskURL = "https://user-images.githubusercontent.com/71917474/101284898-d39a9200-3825-11eb-9474-44084a8631de.jpg"
#print(DB_PATH)

botKey = {
    '선별진료소 안내' : "5fafee1f2cb6e55d5b67a980",
    '자가진단': "5fb0348fd6fe9b32458ce223",
    '전세계 현황': "5fb0e639d9431d64aa840e50",
    '유튜브 뉴스': "5fb0e293d6fe9b32458ce405",
    '네이버 뉴스': "5fb0e29be0729d24a9b0b20a",
    '국내 현황': "5fcbb41d779b4a59a14d4016",
    '근처 병원 및 약국 안내': "5fb08876d9431d64aa840cea",
    '사회적 거리두기 단계': "5fb041a2eb7b236e6162d7e7",
    '재난 문자 현황': "5fb08d08d6fe9b32458ce2a4"
    }

def hotKeywordButton(buttons):
    dataSend = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "carousel": {
                    "type": "basicCard",
                    "items": [
                        {
                            "title":  "인기 키워드",
                            "thumbnail": {
                                "imageUrl": MaskURL},
                            "buttons": buttons
                        }
                    ]
                }
            }
        ]
    }
}
    return dataSend

def dataSendSimple(message):

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText":{
                        "text" : message
                    }
                }
            ]
        }
    }

    return dataSend

def GlobaldataSendCard(nation,message,imageUrl):

    dataSend = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                "title": nation+" 코로나 현황",
                                "description": message,
                                "thumbnail": {
                                    "imageUrl": imageUrl},
                                "buttons": [
                                    {
                                        "action": "share",
                                        "label": "공유하기"}
                                ]
                            }
                        ]
                    }
                }
            ]
        }
    }

    return dataSend


nations = { #key : #value(country_code for db search)
            '전세계':'전세계',
            '아프가니스탄' : 'AF' ,
            '알바니아' : 'AL' ,
            '알제리' : 'DZ' ,
            'Andorra' : 'AD' ,
            'Angola' : 'AO' ,
            'Antigua and Barbuda' : 'AG' ,
            '아르헨티나' : 'AR' ,
            'Armenia' : 'AM' ,
            '호주' : 'AU' ,
            '오스트리아' : 'AT' ,
            'Azerbaijan' : 'AZ' ,
            'Bahamas' : 'BS' ,
            'Bahrain' : 'BH' ,
            '방글라데시' : 'BD' ,
            'Barbados' : 'BB' ,
            'Belarus' : 'BY' ,
            '벨기에' : 'BE' ,
            'Belize' : 'BZ' ,
            'Benin' : 'BJ' ,
            'Bhutan' : 'BT' ,
            'Bolivia' : 'BO' ,
            'Bosnia and Herzegovina' : 'BA' ,
            'Botswana' : 'BW' ,
            '브라질' : 'BR' ,
            'Brunei' : 'BN' ,
            '불가리아' : 'BG' ,
            'Burkina Faso' : 'BF' ,
            'Burma' : 'MM' ,
            'Burundi' : 'BI' ,
            'Cabo Verde' : 'CV' ,
            '캄보디아' : 'KH' ,
            'Cameroon' : 'CM' ,
            '캐나다' : 'CA' ,
            'Central African Republic' : 'CF' ,
            'Chad' : 'TD' ,
            'Chile' : 'CL' ,
            '중국' : 'CN' ,
            '콜롬비아' : 'CO' ,
            'Comoros' : 'KM' ,
            'Congo (Brazzaville)' : 'CG' ,
            'Congo (Kinshasa)' : 'CD' ,
            '코스타리카' : 'CR' ,
            '크로아티아' : 'HR' ,
            '쿠바' : 'CU' ,
            'Cyprus' : 'CY' ,
            '체코' : 'CZ' ,
            '덴마크' : 'DK' ,
            'Diamond Princess' : 'XX' ,
            'Djibouti' : 'DJ' ,
            'Dominica' : 'DM' ,
            'Dominican Republic' : 'DO' ,
            'Ecuador' : 'EC' ,
            '이집트' : 'EG' ,
            'El Salvador' : 'SV' ,
            'Equatorial Guinea' : 'GQ' ,
            'Eritrea' : 'ER' ,
            'Estonia' : 'EE' ,
            'Eswatini' : 'SZ' ,
            'Ethiopia' : 'ET' ,
            'Fiji' : 'FJ' ,
            '핀란드' : 'FI' ,
            '프랑스' : 'FR' ,
            'Gabon' : 'GA' ,
            '잠비아' : 'GM' ,
            '조지아' : 'GE' ,
            '독일' : 'DE' ,
            'Ghana' : 'GH' ,
            '그리스' : 'GR' ,
            'Grenada' : 'GD' ,
            'Guatemala' : 'GT' ,
            'Guinea' : 'GN' ,
            'Guinea-Bissau' : 'GW' ,
            'Guyana' : 'GY' ,
            'Haiti' : 'HT' ,
            'Holy See' : 'VA' ,
            'Honduras' : 'HN' ,
            '헝가리' : 'HU' ,
            '아이슬란드' : 'IS' ,
            '인도' : 'IN' ,
            '인도네시아' : 'ID' ,
            'Iran' : 'IR' ,
            'Iraq' : 'IQ' ,
            '아일랜드' : 'IE' ,
            'Israel' : 'IL' ,
            '이탈리아' : 'IT' ,
            'Jamaica' : 'JM' ,
            '일본' : 'JP' ,
            'Jordan' : 'JO' ,
            'Kazakhstan' : 'KZ' ,
            'Kenya' : 'KE' ,
            '한국' : 'KR' ,
            'Kosovo' : 'XK' ,
            'Kuwait' : 'KW' ,
            'Kyrgyzstan' : 'KG' ,
            'Laos' : 'LA' ,
            'Latvia' : 'LV' ,
            'Lebanon' : 'LB' ,
            'Lesotho' : 'LS' ,
            'Liberia' : 'LR' ,
            'Libya' : 'LY' ,
            'Liechtenstein' : 'LI' ,
            'Lithuania' : 'LT' ,
            'Luxembourg' : 'LU' ,
            'MS Zaandam' : 'XX' ,
            'Madagascar' : 'MG' ,
            'Malawi' : 'MW' ,
            '말레이시아' : 'MY' ,
            'Maldives' : 'MV' ,
            'Mali' : 'ML' ,
            'Malta' : 'MT' ,
            'Marshall Islands' : 'MH' ,
            'Mauritania' : 'MR' ,
            'Mauritius' : 'MU' ,
            '멕시코' : 'MX' ,
            'Moldova' : 'MD' ,
            'Monaco' : 'MC' ,
            'Mongolia' : 'MN' ,
            'Montenegro' : 'ME' ,
            '모로코' : 'MA' ,
            'Mozambique' : 'MZ' ,
            'Namibia' : 'NA' ,
            '네팔' : 'NP' ,
            '네덜란드' : 'NL' ,
            '뉴질랜드' : 'NZ' ,
            'Nicaragua' : 'NI' ,
            'Niger' : 'NE' ,
            'Nigeria' : 'NG' ,
            'North Macedonia' : 'MK' ,
            'Norway' : 'NO' ,
            'Oman' : 'OM' ,
            '파키스탄' : 'PK' ,
            'Panama' : 'PA' ,
            'Papua New Guinea' : 'PG' ,
            'Paraguay' : 'PY' ,
            'Peru' : 'PE' ,
            '필리핀' : 'PH' ,
            '필란드' : 'PL' ,
            '포르투갈' : 'PT' ,
            'Qatar' : 'QA' ,
            'Romania' : 'RO' ,
            '러시아' : 'RU' ,
            'Rwanda' : 'RW' ,
            'Saint Kitts and Nevis' : 'KN' ,
            'Saint Lucia' : 'LC' ,
            'Saint Vincent and the Grenadines' : 'VC' ,
            'San Marino' : 'SM' ,
            'Sao Tome and Principe' : 'ST' ,
            'Saudi Arabia' : 'SA' ,
            '세네갈' : 'SN' ,
            'Serbia' : 'RS' ,
            'Seychelles' : 'SC' ,
            'Sierra Leone' : 'SL' ,
            '싱가폴' : 'SG' ,
            '슬로바키아' : 'SK' ,
            '슬로베니아' : 'SI' ,
            'Solomon Islands' : 'SB' ,
            'Somalia' : 'SO' ,
            'South Africa' : 'ZA' ,
            '남수단' : 'SS' ,
            '스페인' : 'ES' ,
            'Sri Lanka' : 'LK' ,
            '수단' : 'SD' ,
            'Suriname' : 'SR' ,
            '스웨덴' : 'SE' ,
            '스위스' : 'CH' ,
            '시리아' : 'SY' ,
            '대만' : 'TW' ,
            'Tajikistan' : 'TJ' ,
            'Tanzania' : 'TZ' ,
            '태국' : 'TH' ,
            'Timor-Leste' : 'TL' ,
            '토고' : 'TG' ,
            'Trinidad and Tobago' : 'TT' ,
            'Tunisia' : 'TN' ,
            '터키' : 'TR' ,
            '미국' : 'US' ,
            '우간다' : 'UG' ,
            'Ukraine' : 'UA' ,
            '아랍에미리트' : 'AE' ,
            '영국' : 'GB' ,
            '우루과이' : 'UY' ,
            '우즈베키스탄' : 'UZ' ,
            'Vanuatu' : 'VU' ,
            '베네수엘라' : 'VE' ,
            '베트남' : 'VN' ,
            'West Bank and Gaza' : 'PS' ,
            'Western Sahara' : 'EH' ,
            'Yemen' : 'YE' ,
            '잠비아' : 'ZM' ,
            'Zimbabwe' : 'ZW'}

#query create global table
QCT_global  = '''CREATE TABLE IF NOT EXISTS GLOBAL
    (COUNTRY CHAR(20) NOT NULL,
    COUNTRY_CODE CHAR(10) NOT NULL,
    Data    JSON NOT NULL,
    LASTUPDATE  DATETIME);'''

QCT_hotKeyword = '''CREATE TABLE HOTKEYWORD
    (KEYWORD TEXT NOT NULL,
    COUNTING INT NOT NULL);'''

deleteQuery = "Delete From HOTKEYWORD where condition"

QUD_hotKeyword = "UPDATE  HOTKEYWORD SET COUNTING + 1 WHERE KEYWORD = %s"

#Global Data sample request json data
sampleReque = {'bot': {'id': '5fa4d2bf6d34f06b2b08ad93', 'name': 'corona_chatbot'},
'intent': {'id': '5fb0e639d9431d64aa840e50',
'name': '전세계 현황', 'extra': {'reason': {'code': 1, 'message': 'OK'}}},
'action': {'id': '5fb8dd0e06b0fa6d6630322a', 'name': 'globalData',
'params': {'sys_nation': '미국', 'situation': 'situation'},
'detailParams': {'sys_nation': {'groupName': '', 'origin': '미국', 'value': '미국'},
'situation': {'groupName': '', 'origin': '데이터', 'value': 'situation'}},
'clientExtra': {}},
'userRequest': {'block': {'id': '5fb0e639d9431d64aa840e50', 'name': '전세계 현황'},
'user': {'id': '28761f0d6fec519d333afb202d85dca7842acb03053fbc6e77f757a681a0732475',
'type': 'botUserKey', 'properties':
{'botUserKey': '28761f0d6fec519d333afb202d85dca7842acb03053fbc6e77f757a681a0732475',
'isFriend': True, 'plusfriendUserKey': 'IWOvhONHTgXo',
'bot_user_key': '28761f0d6fec519d333afb202d85dca7842acb03053fbc6e77f757a681a0732475',
'plusfriend_user_key': 'IWOvhONHTgXo'}}, 'utterance': '미국 데이터',
'params': {'surface': 'Kakaotalk.plusfriend'}, 'lang': 'ko', 'timezone': 'Asia/Seoul'},
'contexts': []}

print("blockId : "+sampleReque['userRequest']['block']['id'])
