//
//  Login.swift
//  SkillmateLogin
//
//  Created by Carina Chan on 4/15/24.
//

import SwiftUI
import AuthenticationServices

struct Login: View {
    
    var body: some View {
        
        NavigationView {
            
            VStack {
                
                //Skillmate logo
                Image("skillmate_final_part_icon_for_real").resizable().frame(width: 140, height: 150).position(CGPoint(x: 200.0, y: 270.0))
                
                //Skillmate text
                Image("title_text").resizable().frame(width: 250, height: 50).position(CGPoint(x: 200.0, y: 100.0))
                
                //Sign in with Apple button --> No Apple Account
                NavigationLink(destination: NoAppleAcct()) {
                    //Sign in with Apple Button
                    SignInWithAppleButton(.signIn) { request in
                        request.requestedScopes = [.fullName, .email]
                    } onCompletion: { result in
                        switch result {
                        case .success(let authResult):
                            print("Auth success. Result: \(authResult)")
                            //Post-authentication updates on persistence and/or states.
                        case .failure(let error):
                            print("Auth failed. Result: \(error.localizedDescription)")
                            //Handle auth failures
                        }
                    }.frame(width: 280, height: 40, alignment: .center).signInWithAppleButtonStyle(.whiteOutline).position(CGPoint(x: 200.0, y: 10.0))
                }
            }
        }
    }
}


//Preview for page
struct Login_Previews: PreviewProvider {
    static var previews: some View {
        Login()
    }
}
