from ultralytics.utils.benchmarks import ProfileModels, benchmark

ProfileModels(['models/yolov5nu.onnx'], min_time=300).run()
# benchmark(model='models/mrtdetr.onnx', imgsz=160)
