# DownloadTube

Bu Python scripti, videonun kalitesini seçmenize ve indirme konumunu bir GUI klasör seçme penceresi kullanarak belirlemenize olanak tanıyan basit ama güçlü bir YouTube video indiricisidir.

## Özellikler
- **Kalite Seçimi**: Mevcut video kalite seçeneklerinden birini seçin (örneğin, 720p, 1080p).
- **Grafiksel Klasör Seçimi**: İndirilen videoyu kaydedeceğiniz yeri seçmek için bir açılır pencere kullanın.
- **Kullanımı Kolay Konsol Arayüzü**: Sadece YouTube URL'sini girin ve indirmek için talimatları izleyin.

## Gereksinimler
Bu scripti kullanmak için aşağıdaki Python modüllerine ihtiyacınız var:

- **yt-dlp**: YouTube videolarını indirmek için youtube-dl'nin daha güncel bir çatalı.
- **Tkinter**: Klasör seçimi için GUI kullanılır.
- **termcolor**: Konsol mesajlarına renk ve biçimlendirme eklemek için kullanılır.

Bu bağımlılıkları aşağıdaki komutla yükleyebilirsiniz:

```sh
pip install yt-dlp termcolor
```

## Nasıl Kullanılır
1. Bu depoyu klonlayın veya scripti doğrudan indirin.
2. Gerekli bağımlılıkların kurulu olduğundan emin olun.
3. Scripti aşağıdaki komutla çalıştırın:

```sh
python downloadtube.py
```

4. İstenildiğinde YouTube video URL'sini girin.
5. İstediğiniz video kalitesini seçin.
6. Videoyu kaydetmek istediğiniz klasörü açılır pencereyi kullanarak seçin.
7. Video indirilmeye başlanacak ve seçilen klasöre kaydedilecektir.

## Çalıştırılabilir Dosyaya Dönüştürme
Bu Python scriptini bağımsız bir `.exe` dosyasına dönüştürmek için `PyInstaller` kullanabilirsiniz. İşte nasıl yapılacağı:

1. `PyInstaller`'ı yükleyin:
   ```sh
   pip install pyinstaller
   ```
2. Aşağıdaki komutu çalıştırarak çalıştırılabilir dosyayı oluşturun:
   ```sh
   pyinstaller --onefile downloadtube.py
   ```
3. `.exe` dosyası `dist` klasöründe bulunacaktır.

## Örnek
```
YouTube video URL'sini girin: https://www.youtube.com/watch?v=dQw4w9WgXcQ

Mevcut Kalite Seçenekleri:
[0] 360p - mp4
[1] 720p - mp4

Lütfen istediğiniz kalite numarasını girin: 1

Video indiriliyor...

Video başarıyla indirildi: C:\Users\User\Downloads
```

## Not
- En iyi deneyim için `yt-dlp`'nin en son sürümünü kullandığınızdan emin olun.
- Eğer bir klasör seçilmezse, script otomatik olarak geçerli klasörü kullanacaktır.

## Lisans
Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

## Katkılar
Katkılar memnuniyetle kabul edilir! Depoyu çatallayıp bir pull request gönderebilirsiniz.

## Sorumluluk Reddi
Bu araç yalnızca kişisel kullanım içindir. Herhangi bir video indirmeden önce YouTube'un hizmet şartlarına uyduğunuzdan emin olun.

