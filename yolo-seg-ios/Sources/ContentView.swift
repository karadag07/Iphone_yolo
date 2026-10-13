import SwiftUI
import YOLO

struct ContentView: View {
    var body: some View {
        // Models/yolo11n-seg.mlpackage dosyasi GitHub Actions tarafindan uretilir.
        YOLOCamera(
            modelPathOrName: "yolo11n-seg",
            task: .segment,
            cameraPosition: .back
        )
    }
}
