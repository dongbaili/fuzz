file=test # Replace with your desired file name without extension
cd arkcompiler/runtime_core/static_core
echo "Compiling $file.ets"
./out/bin/es2panda $file.ets --output $file.abc

echo "Running $file.abc"
./out/bin/ark --boot-panda-files=./out/plugins/ets/etsstdlib.abc --load-runtimes=ets $file.abc $file.ETSGLOBAL::main
