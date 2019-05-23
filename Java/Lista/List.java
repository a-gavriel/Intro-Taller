/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication1;

import javaapplication1.Node;

/**
 *
 * @author user
 */
public class List {
    public Node head;
    
    public List(){
    }
    
    
    public void insert(float x){
      Node newnode = new Node(x);
      newnode.next = null;
      
      if (head == null){
          head = newnode;
      }else{
          Node last = head;
          while(last.next != null){
              last =  last.next;
          }
          last.next = newnode;          
      }       
    }
    
    public void printList() { 
        Node currNode = head; 
   
        System.out.print("LinkedList: "); 
   
        // Traverse through the LinkedList 
        while (currNode != null) { 
            // Print the data at current node 
            System.out.print(currNode.data + " "); 
   
            // Go to next node 
            currNode = currNode.next; 
        }
        System.out.println("");
    } 
    
    public static float getSum(List lista){
        Node current = lista.head;
        
        float result = 0;
        
        while(current != null){
            result += current.data;
            
            current = current.next;
        }
        
        
        return result;
    }
    
    
    
}

 