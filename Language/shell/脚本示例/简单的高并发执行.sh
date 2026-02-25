func_cmd(){
        echo "start $i"
        sleep 5
        echo "end $i"
}

for i in `cat for_list`; do
        func_cmd &
        sleep 0.5
done
