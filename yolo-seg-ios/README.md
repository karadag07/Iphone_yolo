# YoloSeg iOS

iPhone kamerasiyla gercek zamanli YOLO11 segmentasyonu yapan uygulama.
Model ve IPA, GitHub Actions (macOS runner) uzerinde otomatik uretilir.

## Kurulum

1. GitHub'da yeni bir repo ac (ornek: `yolo-seg-ios`) ve bu klasorun icerigini yukle.
2. `main` dalina push edince **Actions** sekmesinde "Build IPA" calisir (yaklasik 10-15 dk).
   Elle baslatmak icin: Actions > Build IPA > Run workflow.
3. Is bitince calismanin sayfasindan **YoloSeg-ipa** artifact'ini indir, zip'ten `YoloSeg.ipa` cikar.

## iPhone'a yukleme (Sideloadly)

1. iPhone'da **Ayarlar > Gizlilik ve Guvenlik > Gelistirici Modu**'nu ac, telefon yeniden baslar.
2. iPhone'u USB ile bilgisayara bagla, "Bu bilgisayara guven" de.
3. Sideloadly'yi ac, `YoloSeg.ipa` dosyasini surukle, Apple ID'ni gir, **Start**'a bas.
4. iPhone'da **Ayarlar > Genel > VPN ve Cihaz Yonetimi**'nden Apple ID profilini "Guven" olarak isaretle.
5. Uygulamayi ac, kamera iznini ver.

Ucretsiz Apple ID ile yuklenen uygulama 7 gun sonra sona erer; Sideloadly ile tekrar yuklemen yeterli.

## Model degistirme

`export_model.py` icinde `MODEL` degerini degistir (ornek: `yolo11s-seg`)
ve `Sources/ContentView.swift` icindeki `modelPathOrName` ismini ayni yap.
