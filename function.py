import cv2
carplate_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
#carplate_haar_cascade = cv2.CascadeClassifier(+"haarcascade_russian_plate_number.xml")
class plate:
    def detect(image):
        carplate_overlay = image.copy() 
        carplate_rects = carplate_haar_cascade.detectMultiScale(carplate_overlay,scaleFactor=1.1, minNeighbors=3)
        for x,y,w,h in carplate_rects: 
            cv2.rectangle(carplate_overlay, (x,y), (x+w,y+h), (255,0,0), 5)        
        return carplate_overlay

    def extract(image):
        carplate_rects = carplate_haar_cascade.detectMultiScale(image,scaleFactor=1.1, minNeighbors=5)
        for x,y,w,h in carplate_rects: 
            carplate_img = image[y+10:y+h-10 ,x+10:x+w-15]        
        return carplate_img

    def enlarge_img(image, scale_percent):
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        return resized_image

    def region(text: str):
        regions={"1": "ADRAR","2":"CHLEF","3":"LAGHOUAT","4":"OUM BOUAGHI","5":"BATNA","6":"BEJAIA",
                "7":"BISKRA","8":"BECHAR","9":"BLIDA","10":"BOUIRA","11":"TAMANRASSET",
                "12":"TEBESSA","13":"TLEMCEN","14":"TIARET","15":"TIZI OUZOU","16":"ALGER",
                "17":"DJELFA","18":"JIJEL","19":"SETIF","20":"SAIDA","21":"SKIKDA","22":"SIDI BEL ABBES","23":"ANNABA","24":"GUELMA",
                "25":"CONSTANTINE","26":"MEDEA","27":"MOSTAGANEM","28":"M'SILA","29":"MASCARA","30":"OUARGLA","31":"ORAN","32":"EL BAYDH",
                "33":"ILLIZI","34":"BORDJ BOU ARRERIDJ","35":"BOUMERDES","36":"EL TAREF","37":"TINDOUF","38":"TISSEMSILT","39":"EL OUED",
                "40":"KHENCHLA","41":"SOUK AHRASS","42":"TIPAZA","43":"MILA","44":"AÏN DEFLA","45":"NÂAMA","46":"AÏN TEMOUCHENT","47":"GHARDAÏA","48":"RELIZANE"}
        return regions[text]

    def type_vehicule(text: str):
        types={"1": "vehicule particulier", "2": "camion", "3": "camionette", "4": "autobus", 
                "5": "tracteur routier", "6": "tracteur", "7": "vehicule special", "8": "remorque", "9": "moto"}
        return types[text]