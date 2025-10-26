from ultralytics.utils.benchmarks import ProfileModels, benchmark

ProfileModels(['models/mrtdetr.onnx']).run()
# benchmark(model='models/mrtdetr.onnx', imgsz=160)