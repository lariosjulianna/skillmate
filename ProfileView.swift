//
//  ProfileView.swift
//  Group4Skillmate
//
//  Created by Dylan Calderon on 4/15/24.
//

import SwiftUI

struct ProfileView: View {
    @State private var isSettingsPresented = false
    
    var body: some View {
        TabView {
            NavigationView {
                Text("Home")
                    .navigationBarTitle("Home")
            }
            .tabItem {
                Label("Home", systemImage: "house.fill")
                    .padding()
            }
            
            NavigationView {
                MessagesView()
                    .navigationBarTitle("Messages")
            }
            .tabItem {
                Label("Messages", systemImage: "message.fill")
                    .padding()
            }
            
            NavigationView {
                VStack {
                    Image(systemName: "person.crop.circle.fill")
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                        .frame(width: 120, height: 120)
                        .padding()
                    
                    Text("Dylan Calderon, 20")
                        .font(.title)
                        .fontWeight(.bold)
                        .padding(.bottom, 10)
                    
                    Text("Software Developer")
                        .font(.headline)
                        .foregroundColor(.gray)
                    
                    HStack(spacing: 20) {
                        CircleButton(label: "Settings", systemImageName: "gearshape.fill") {
                            isSettingsPresented.toggle()
                        }
                        
                        CircleButton(label: "Profile", systemImageName: "person.fill") {
                            // Action for Profile button
                        }
                        
                        CircleButton(label: "Privacy", systemImageName: "shield.fill") {
                            // Action for Privacy button
                        }
                    }
                    .padding(.top, 20)
                    .sheet(isPresented: $isSettingsPresented) {
                        SettingsView()
                    }
                }
                .padding()
                .navigationBarTitle("Profile")
            }
            .tabItem {
                Label("Profile", systemImage: "person.fill")
                    .padding()
            }
        }
    }
}


struct ProfileView_Previews: PreviewProvider {
    static var previews: some View {
        ProfileView()
    }
}

struct CircleButton: View {
    let label: String
    let systemImageName: String
    let action: () -> Void
    
    var body: some View {
        VStack {
            Button(action: action) {
                Image(systemName: systemImageName)
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(width: 40, height: 40)
                    .foregroundColor(.black) // Set icon color to black
            }
            Text(label)
                .foregroundColor(.black) // Set label font color to black
                .font(.caption)
        }
        .frame(width: 80, height: 100)
        .background(
            LinearGradient(gradient: Gradient(colors: [Color.white.opacity(0.2), Color.white.opacity(0.1)]), startPoint: .topLeading, endPoint: .bottomTrailing)
        )
        .clipShape(Circle())
        .overlay(
            Circle()
                .stroke(Color.black, lineWidth: 2)
        )
    }
}
