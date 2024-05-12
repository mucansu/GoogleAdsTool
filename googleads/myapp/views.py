from django.shortcuts import render
from django.http import HttpResponse
import google.generativeai as genai


# Create your views here.


#Burda basitçe google reklam için yapay zeka yardımıyla içerik üretiyoruz. 


# genai.configure("AIzaSyCTGAhacGU6cauPEB_eyc5lfMzeVxiiAJg")
genai.configure(api_key="")

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
#def mkesik(request):
 #   return render(request,"mkesik.html")
def index(request):
    if request.method == 'POST':
        # Extract data from the form submission
        title_number = request.POST.get('title-number')
        title_char_count = request.POST.get('title-char-count')
        title_instructions= request.POST.get('title-instructions')
        keywords_number = request.POST.get('keywords-number')
        keyword_detail = request.POST.get('keyword_detail')
        keywords_char_count = request.POST.get('keywords-char-count')
        description_text_number = request.POST.get('description-text-number')
        description_text_char_count = request.POST.get('description-tex-char-count')
        description_text_instructions =  request.POST.get('title-instructions')
        company = request.POST.get('company')
        service = request.POST.get('service')
        target = request.POST.get('target')
        input = request.POST.get('input-text')
    #if request.method == 'POST':
     #   company="ENC Mimarlık ve Mühendislik"
      #  service="ev ve villa komple tadilatı"
       # target="İstanbul'da hizmet veren bu firma evini yenilemek isteyen kişilere bu hizmeti sunuyor"
       # detail="Firmanın artısı, ücretsiz keşif imkanı var. Ayrıca iç mimar tarafından tadilat ve dekorasyon işlemi yapılacağı için mmimari olarak da harika sonuçlar elde ediliyor."
       # keyword_detail="Komple ev tadilatı hizmeti veriyor. Özellikle Beşiktaş, Kadıköy, Ümraniye, Şişli, Beykoz, Üsküdar ilçelerinde hizmet vermek istiyor. Oda dekorasyon hizmeti vermiyor."
    

# Dananın kuyruğunun koptuğu yer burası. Burda belli bir prompt listesi tanımlıyoruz,
# Yapay zekayı beslediğimiz yer burası, istediğimiz reklam ile ilgili bilgi vermemiz lazım.
# Mesela aşağıdaki örnekte dijital pazarlama ile ilgili görevler ve girdiler verdim.
# Kullandığımız yapay zeka modelinden bunları bilmesini isteyerek bana nasıl bir metin,içerik,kelime vermesini
# tembihledim, bazen sapıtabilir, ama kullandıkça sapıtmalarına kürek vurabiliriz.

        prompt_parts = [
    "Dijital web pazarlamacısısın. Gireceğim hizmet alanı ve ürün açıklamaları için,"
    f"Ürün Başlığı: Google aramalarında öne çıkaracak google ads arama ağı reklam yapısına uygun, "
    f" şu talimatları dikkate alarak : {title_instructions} maksimum {title_char_count} karakterden oluşan  {title_number} adet ürün başlığı,"
    f"Ürün Açıklaması : {description_text_number} adet maksimum {description_text_char_count} karakterden oluşan kısa ürün açıklaması, {description_text_instructions},"
    f"Ürün Anahtar kelimeleri: maksimum {keywords_char_count} karakterden oluşan toplam {keywords_number} adet, {keyword_detail} Bunları da dikkate alarak anahtar kelimeler hazırla"
    f"{company} şirketinin sunduğu hizmetler: {service}. hedef kitlesi : {target}. {input}, lütfen her çıktının yanına karakter sayısını yaz."
    f"Başlık,Anahtar Kelime gibi her grubu ayrı başlıklar halinde ver"
    f"Herhangi bir özellik veya sayı belirtmediğim durumlarda en optimum kalite,özgünlük ve sayıyı bul ve istediğim içeriği ona göre üret"
]   
        response = model.generate_content(prompt_parts)
        print(response.text)
        context = {}
        context['response'] = response  # Pass the entire response as a string
        return render(request, 'index.html', context)
        # Split the response into sections
       # sections = response.text.split("**")
       # formatted_response = [section.strip() for section in sections if section.strip()]
       # return render(request, 'index.html', {'response': formatted_response}, {'sections': sections})
        # Extract data from request.POST and interact with your API
        return render(request, 'index.html', {'response': response.text})
    return render(request, 'index.html')

