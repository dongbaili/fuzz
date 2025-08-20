file=modified_test 
echo "Running $file.abc"
./out/bin/ark --boot-panda-files=./out/plugins/ets/etsstdlib.abc --load-runtimes=ets $file.abc test.ETSGLOBAL::main
