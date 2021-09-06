echo "Rekovery LOG - Selezionata modalita' offline"

#Shold implement auto expansion of tilde (since bash doesn't support it) so that is possible to store path into a variable and change it to whole file dinamically
name=$(date)
name="${name// /}"

if [ -d ~/Videos/rekoveryOffline/ ]
then
    echo "Rekovery LOG - Cartella di output esistente!"
    echo "Rekovery LOG - Registrazione avviata..."
    raspivid -n -t 0 -h 1080 -w 1920 -o ~/Videos/rekoveryOffline/"$name".h264
    
else
    echo "Rekovery LOG - Creo cartella di output"
    mkdir ~/Videos/rekoveryOffline/
    echo "Rekovery LOG - Registrazione avviata..."
    raspivid -n -t 0 -h 1080 -w 1920 -o ~/Videos/rekoveryOffline/"$name".h264 
    
fi  