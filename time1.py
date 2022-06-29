import time 

time.gmtime(0) #işletim sisteminin referans aldığı başlangıç tarihini alır

time.time() #bu fonksiyon ile başlangıç zamanından şu anki zamana kadar geçen zamanın saniye cinsinden değeri verilir

time.localtime() #anlık saat tarih ve zaman bilgisini struct_time nesnesi olarak verir

time.asctime() #bugünün tarih saat ve zaman bilgisini verir

time.strftime() #datetime modulündeki strftime ile aynıdır. biçimlendiriciler kullanmaktadır

time.strptime() #datetime modulündeki strptime ile aynıdır. veri biçimlendirmek içib kullanılır. strfden farkı, veri belirtmemiz

time.sleep() #bu fonksiyon ile yazılan kodların işleyişi belirli bir süre beklemeye alınır. int türünden parametre alır