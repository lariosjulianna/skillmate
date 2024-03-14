//
//  ContentView.swift
//  SkillMate_UI
//
//  Created by daisy fernandez-reyes on 3/14/24.
//

import SwiftUI
import UIKit

struct ContentView: View {
    
    var body: some View {
        VStack {
            Image("skillmate_macos_16")
            
            
            Button(action: {
                // Action for your login button
                print("Login button tapped")
            }) {
                Text("Login")
                    .font(.custom("Merriweather-Black", size:12))
                //figure out fonts
                    .foregroundColor(.white) // Text color
                    .padding() // Add padding around the text
                    .frame(height: 50) // Specific height for the button
                    .frame(width: 75)
                    .background(LinearGradient(gradient: Gradient(colors: [Color.skillBlue, Color.skillLime]), startPoint: /*@START_MENU_TOKEN@*/.leading/*@END_MENU_TOKEN@*/, endPoint: /*@START_MENU_TOKEN@*/.trailing/*@END_MENU_TOKEN@*/)) // Button background color
                    .cornerRadius(12) // Rounded corners
                    .overlay(
                        RoundedRectangle(cornerRadius: 12)
                            .stroke(Color.clear, lineWidth: 1.5) // Border
                    )
            }
        }
    }
    }
        

#Preview {
    ContentView()
}
