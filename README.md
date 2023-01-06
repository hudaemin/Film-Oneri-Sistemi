# Film Oneri Sistemi
 
  Öneri sistemleri, genellikle bir film veri tabanındaki diğer filmlerle karşılaştırarak benzerlikleri ölçer ve bu benzerliklere göre öneriler yapar ve bu sayede kullanıcıların ilgi alanlarına uygun filmleri keşfetmelerine yardımcı olur ve bu şekilde film izleme deneyimlerini zenginleştirir. Bu sistemi kullanarak kullanıcılar sevdikleri bir filme göre 30 film tavsiyesi alabilir.

Flask ve Python modülleri kullanarak önceki izlenen film baz alınarak yeni 30 film öneren bir site tasarladım. Bu projede Excelden veriler okunuyor. Bu veri setini internette buldum. Excel’de saklanan bu veri sitesinde 4803 adet film listeleniyor. Her film 24 için 24 ayrı parametre bulunuyor. Filmlerin isimleri, yönetmenleri, oyuncuları, yapım şirketlerinin isimleri, orijinal dilleri, bütçeleri, konuları, çıkış tarihleri ve türleri gibi birçok bilgi bulunuyor. Bu projede birçok python kütüphanesi kullandım, bunlar; Pandas, Difflib, Flask ve Sklearn.
 
Pandas, Python'da veri manipülasyonu ve analizi için kullanılan bir kütüphanedir. Bu kod parçacığında, pandas kütüphanesi ile movies.csv dosyasını okuyor ve verileri movies_data adlı bir veri çerçevesine yüklüyorsunuz.


Difflib, Python'da benzerlik oranı hesaplamak için kullanılan bir kütüphanedir. Bu kod parçacığında, get_close_matches fonksiyonu ile bir film isminin en yakın eşleştirilen film ismi bulunmaktadır.


Sklearn, scikit-learn adıyla da bilinen, Python dilinde machine learning algoritmalarının kullanımını kolaylaştıran bir kütüphanedir. Bu kod parçacığında, TfidfVectorizer ve cosine_similarity modülleri sklearn kütüphanesinden import edilmiştir. TfidfVectorizer, metin verilerini özellik vektörlerine dönüştürürken kullanılmıştır. Cosine_similarity ise iki vektörün benzerliğini ölçmek için kullanılmıştır. TfidfVectorizer ile metin verileri özellik vektörlerine dönüştürülür ve cosine_similarity ile bu özellik vektörlerinin benzerliği hesaplanır. Bu sayede, kullanıcının girdiği film ismine en yakın eşleşen filmler bulunarak önerilebilir.


Flask, Python dilinde yazılmış, çok hafif bir web framework'üdür. Web frameworkleri, web uygulamalarının geliştirilmesi için kullanılan yazılım araçlarıdır ve genellikle HTTP isteklerini işleme, veri tabanı erişimini yönetme gibi işlemleri otomatikleştirirler. Flask, Python diline entegre olması nedeniyle kolay bir şekilde kullanılabilir ve Python ile birlikte kullanıldığında, web uygulamalarının geliştirilmesi için ideal bir araçtır. Bundan dolayı websitemi oluştururken Flask kullanmayı tercih ettim.
 


![Screenshot_1](https://user-images.githubusercontent.com/64445154/211108855-555510a1-47cc-411a-ac93-4502f933d35a.png)
![Screenshot_5](https://user-images.githubusercontent.com/64445154/211108854-6218cc64-cfa8-4989-b3b2-04393aa3adc6.png)

![Screenshot_2](https://user-images.githubusercontent.com/64445154/211108856-33e39d6e-621f-4674-b5ad-f370d3aa53ff.png)

![Screenshot_3](https://user-images.githubusercontent.com/64445154/211108853-72fa5c9c-17fe-40de-8589-64611f8ad6cf.png)
