//
//  ContentView.swift
//  Skillmate
//
//  Created by madi tansy on 2/28/24.
//

import SwiftUI
import Alamofire

struct ContentView: View {
    var body: some View {
        NavigationView {
            VStack {
                // Your existing content here
                
                Spacer()
                
                WelcomeButtons()
            }
            .navigationTitle("Skillmate App")
        }
    }
}

struct WelcomeButtons: View {
    var body: some View {
        VStack(spacing: 20) {
            NavigationLink(destination: LoginView()) {
                Text("Login")
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }
            
            NavigationLink(destination: SignUpView()) {
                Text("Sign Up")
                    .padding()
                    .background(Color.green)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }
            
            Button(action: {
                exit(0)
            }) {
                Text("Exit")
                    .padding()
                    .background(Color.red)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }
        }
        .padding()
    }
}

struct LoginView: View {
    @State private var email = ""
    @State private var password = ""
    @State private var isLoggedIn = false
    
    var body: some View {
        VStack {
            TextField("Email", text: $email)
                .padding()
            SecureField("Password", text: $password)
                .padding()
            
            Button("Login") {
                login()
            }
            .padding()
        }
        .padding()
        .onAppear {
            // Additional logic to navigate to a different view if already logged in
            // For example, you can use `NavigationLink` or other navigation techniques
            if isLoggedIn {
                print("Already logged in. Welcome!")
            }
        }
    }
    
    func login() {
        let url = "http://localhost:3000/login"
        let parameters: [String: Any] = ["email": email, "password": password]
        
        AF.request(url, method: .post, parameters: parameters, encoding: JSONEncoding.default)
            .validate()
            .responseDecodable(of: UserResponse.self) { response in
                switch response.result {
                case .success(let userResponse):
                    isLoggedIn = true
                    print("Logged in successfully. Welcome, \(userResponse.firstname)!")
                case .failure(let error):
                    print("Error logging in:", error)
                }
            }
    }
}

struct SignUpView: View {
    @State private var email = ""
    @State private var password = ""
    @State private var firstname = ""
    @State private var lastname = ""
    
    var body: some View {
        VStack {
            TextField("Email", text: $email)
                .padding()
            SecureField("Password", text: $password)
                .padding()
            TextField("First Name", text: $firstname)
                .padding()
            TextField("Last Name", text: $lastname)
                .padding()
            
            Button("Sign Up") {
                createAccount()
            }
            .padding()
        }
        .padding()
    }
    
    func createAccount() {
        let url = "http://localhost:3000/createUser"
        let parameters: [String: Any] = ["email": email, "password": password, "firstname": firstname, "lastname": lastname]
        
        AF.request(url, method: .post, parameters: parameters, encoding: JSONEncoding.default)
            .validate()
            .response { response in
                switch response.result {
                case .success:
                    print("Account created successfully!")
                case .failure(let error):
                    print("Error creating account:", error)
                }
            }
    }
}

struct UserResponse: Decodable {
    let firstname: String
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
