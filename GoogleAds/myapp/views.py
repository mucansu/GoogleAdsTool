from django.shortcuts import render
from django.http import HttpResponse
import google.generativeai as genai


# Create your views here.


#Burda basitçe google reklam için yapay zeka yardımıyla içerik üretiyoruz. 


# genai.configure("AIzaSyCTGAhacGU6cauPEB_eyc5lfMzeVxiiAJg")
genai.configure(api_key="AIzaSyCTGAhacGU6cauPEB_eyc5lfMzeVxiiAJg")

# burada kullanacağımız yapay zekanın yaratıcılık ve üst limitini belirleyeceğiz
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
# Zararlı içerikleri engelleme ayarları 
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]
#burası muhtemelen hiç değişmeyecek, kullandığımız yapay zekanın yeni modelleri çıkmadığı sürece.
model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)









# x=response.text
# i1=x.find("**Ürün Açıklaması:**")
# i2=x.find("**Ürün Anahtar Kelimeleri:**")

# s1=x[i1:i2]
# ss1=s1.split("\n")
# print(ss1)
# for s in ss1:
#     i=s.find(" ")
#     s=s[i:]
def mkesik(request):
    return render(request,"mkesik.html")
def index(request):
    if request.method == 'POST':
        company="ENC Mimarlık ve Mühendislik"
        service="ev ve villa komple tadilatı"
        target="İstanbul'da hizmet veren bu firma evini yenilemek isteyen kişilere bu hizmeti sunuyor"
        detail="Firmanın artısı, ücretsiz keşif imkanı var. Ayrıca iç mimar tarafından tadilat ve dekorasyon işlemi yapılacağı için mmimari olarak da harika sonuçlar elde ediliyor."
        keyword_detail="Komple ev tadilatı hizmeti veriyor. Özellikle Beşiktaş, Kadıköy, Ümraniye, Şişli, Beykoz, Üsküdar ilçelerinde hizmet vermek istiyor. Oda dekorasyon hizmeti vermiyor."
    

# Dananın kuyruğunun koptuğu yer burası. Burda belli bir prompt listesi tanımlıyoruz,
# Yapay zekayı beslediğimiz yer burası, istediğimiz reklam ile ilgili bilgi vermemiz lazım.
# Mesela aşağıdaki örnekte dijital pazarlama ile ilgili görevler ve girdiler verdim.
# Kullandığımız yapay zeka modelinden bunları bilmesini isteyerek bana nasıl bir metin,içerik,kelime vermesini
# tembihledim, bazen sapıtabilir, ama kullandıkça sapıtmalarına kürek vurabiliriz.

        prompt_parts = [
    "Dijital web pazarlamacısısın. Gireceğim hizmet alanı ve ürün açıklamaları için, Ürün Başlığı: Google "
    "aramalarında öne çıkaracak google ads arama ağı reklam yapısına uygun 10 adet ürün başlığı, 10 adet 90 karakterden kısa ürün açıklaması Ürün Açıklaması: Google aramalarında öne çıkaracak maksimum 50 "
    f"kelimelik ürün açıklaması, Ürün Anahtar kelimeleri: 50 adet anahtar kelime hazırlayabilir misin? {keyword_detail} Bunları da dikkate alarak anahtar kelimeler hazırlar mısın?",
    f"input: {company} şirketinin sunduğu hizmetlerden biri {service}. {target}. {detail}"
    "siteleri",
    "Ürün Başlığı:  ",
]   
        response = model.generate_content(prompt_parts)
        print(response.text)
        # Extract data from request.POST and interact with your API
        return render(request, 'index.html', {'response': response})
    return render(request, 'index.html')

