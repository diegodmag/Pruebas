#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/**
 * Clase que modela una solicitud  
 */
class solicitud{
    string origen; 
    string destino; 
    string usuario; 

public:

    solicitud(string o, string d, string u){
        origen = o; 
        destino = d; 
        usuario = u; 
    }

void mostrarSolcitud(){
    cout << "Origen: " << origen << "\n" << "Destino: " << destino << "\n" << "Usuario: " << usuario << endl; 
}

string getOrigen(){
    return origen;
}


string getDestino(){
    return destino;
}


string getUsuario(){
    return usuario;
}

};

/**
 * Metodo que recibe una lista de solicitudes, crea un iterador a partir de esa lista 
 * y la recorre para aplicar el metodo de mostrarSolicitud de la clase solicitud
 */
void mostrarSolicitudes(list<solicitud> l){
    //Creacion del iterador de una lista de solicitud 
    list<solicitud>::iterator it;
    for(it=l.begin();it!=l.end();it++)
   {
       it->mostrarSolcitud();
       cout << "--------" << endl; 
   }
   cout << "\n";
}

/**
 * Metodo que fusiona dos listas de solicitudes y regresa la union de estas alternando su elementos 
 */
list<solicitud> fusionarSolicitudes(list<solicitud> l1, list<solicitud> l2){
        
        // Lista que se va a regresar 
        list<solicitud> fusion; 

        int long1 = l1.size();
        int long2 = l2.size();

 
        //Se crea un iterador para cada lista y se inicializa 
        list<solicitud>::iterator it1 = l1.begin();
        list<solicitud>::iterator it2 = l2.begin();

        //Consideramos a la lista de mayor tamanio para concatenar ambas listas de forma alternada 

        if(l1.size() >= l2.size()){
            while (it1 != l1.end())
            {
                fusion.push_back(*it1);
                ++it1; 
                if(it2 != l2.end()){
                    fusion.push_back(*it2);
                    ++it2; 
                }
            }
            
        }

        if(l1.size() < l2.size()){
            while (it2 != l2.end())
            {
                fusion.push_back(*it2);
                ++it2; 
                if(it1 != l1.end()){
                    fusion.push_back(*it1);
                    ++it1; 
                }
            }
            
        }
            
        
        
        return fusion; 
}

list<solicitud> compatir(list<solicitud> l1, list<solicitud> l2){
            // Lista que se va a regresar 
    list<solicitud> inter; 

    int long1 = l1.size();
    int long2 = l2.size();

 
        //Se crea un iterador para cada lista y se inicializa 
        list<solicitud>::iterator it1 = l1.begin();
        list<solicitud>::iterator it2 = l2.begin();

        //Consideramos a la lista de mayor tamanio para concatenar ambas listas de forma alternada 
        for (; it1 != l1.end() && it2 != l2.end(); ++it1, ++it2)
        {   
            string origen1 = *it1->getOrigen(); 
            string origen2 = *it2->getOrigen(); 

            string destino1 = *it1->getDestino(); 
            string destino2 = *it2->getOrigen();    

            if(origen1.compare(origen2)==0 && destino1.compare(destino2)==0 ){
                inter.push_back(*it1);
                inter.push_front(*it2); 
            }

                
        }
        
    return inter;
}



class comparteVehiculo{

    

};


int main()
{ 
    // COMENTARIO GENERICO PARA COMITEAR 
    
   //Primera lista 
   //Se crean las solicitudes 
   solicitud s1("Puebla", "CDMX", "Juan");
   solicitud s2("Oaxaca", "CDMX", "Pedro");
   solicitud s3("Chiapas", "CDMX", "ELGIO");

    //Se crea una lista de solicitudes 
   list<solicitud> solicitudes; 

    //Se agregan las solicitudes a la lista 
    solicitudes.push_front(s1);
    solicitudes.push_front(s2);
    solicitudes.push_front(s3);

    mostrarSolicitudes(solicitudes);

    cout << "********"<< endl; 

    //Segunda lista 

    list<solicitud> solicitudes2;
   solicitud s4("Puebla", "Guerrero", "Juana");
   solicitud s5("Oaxaca", "Sonora", "Pietra");
   solicitud s6("CDMX", "CDMX", "HUGO");
   solicitud s7("CDMX", "Neverwhere", "William");


    solicitudes2.push_front(s4);
    solicitudes2.push_front(s5);
    solicitudes2.push_front(s6);
    solicitudes2.push_back(s7);

    mostrarSolicitudes(solicitudes2); 
    cout << "********"<< endl;

    //Probando la funsion de listas 

    list<solicitud> nueva = fusionarSolicitudes(solicitudes, solicitudes2); 
    mostrarSolicitudes(nueva);

   return 0; 
}