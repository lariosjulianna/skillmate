//
//  NoAppleAcct.swift
//  SkillmateLogin
//
//  Created by Carina Chan on 4/18/24.
//

import SwiftUI

struct NoAppleAcct: View {
    
    //Text variables
    @State var textOops: String = "Oops!"
    @State var textNoAcct: String = "We couldn't find a skillmate account connected to that Apple Account."
    
    var body: some View {
        
        NavigationView {
            
            VStack {
                
                //"Oops!" text
                TextEditor(text: $textOops)
                    .font(.system(size: 40))
                    .multilineTextAlignment(.center)
                    .position(CGPoint(x: 200.0, y: 250.0))
                
                //No account text
                TextEditor(text: $textNoAcct)
                    .font(.system(size: 20))
                    .multilineTextAlignment(.center)
                    .position(CGPoint(x: 200.0, y: 250.0))
                
                //Create new account button
                Button(action: /*@START_MENU_TOKEN@*/{}/*@END_MENU_TOKEN@*/, label: {
                    Text("Create new account".uppercased())
                        .foregroundColor(.white)
                        .padding()
                        .frame(width: 250, height: 50)
                        .background(Color.orange)
                        .cornerRadius(10)
                        .position(CGPoint(x: 200.0, y: 200.0))
                })
                
                //Skillmate logo
                Image("skillmate_final_part_icon_for_real").resizable().frame(width: 45, height: 50).position(CGPoint(x: 200.0, y: -480.0))
            }
        }
    }
}


//Preview for page
struct NoAppleAcct_Previews: PreviewProvider {
    static var previews: some View {
        NoAppleAcct()
    }
}
