/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication1;

/**
 *
 * @author user
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        System.out.println("Hola mundo");
        
        List lista = new List();
        
        float x = 0;
        while ((x < 50) && (x < 100) ){
            float t_n = e_n(x);
            
            lista.insert(t_n);
            
            ++x;
        } 
        
        
        
        float y = List.getSum(lista);
        
        System.out.println(y);
        
        

        
        
        
        
    }
   
    
    
    public static float e_n(float n){
        
        float y = 1;
        // Factorial de n
        while(n>1){
            y *= n;
            --n;
        }
        
        
        
        
        return 1/y;
    }
    
    
}
