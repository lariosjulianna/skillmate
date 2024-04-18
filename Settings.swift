//
//  Settings.swift
//  Group4Skillmate
//
//  Created by Dylan Calderon on 4/16/24.
//

import SwiftUI

struct SettingsView: View {
    var body: some View {
        NavigationView {
            List {
                Section(header: Text("Account")) {
                    NavigationLink(destination: AccountSettingsView()) {
                        Text("Account Settings")
                    }
                    NavigationLink(destination: PrivacySettingsView()) {
                        Text("Privacy Settings")
                    }
                }
                
                Section(header: Text("App")) {
                    NavigationLink(destination: AppSettingsView()) {
                        Text("App Settings")
                    }
                    NavigationLink(destination: AboutView()) {
                        Text("About")
                    }
                }
            }
            .navigationBarTitle("Settings")
        }
    }
}

struct AccountSettingsView: View {
    var body: some View {
        Text("Account Settings")
    }
}

struct PrivacySettingsView: View {
    var body: some View {
        Text("Privacy Settings")
    }
}

struct AppSettingsView: View {
    @AppStorage("isDarkMode") private var isDarkMode = false
    
    var body: some View {
        VStack {
            Toggle("Dark Mode", isOn: $isDarkMode)
                .padding()
        }
        .onChange(of: isDarkMode) { newValue in
            if let windowScene = UIApplication.shared.windows.first?.windowScene {
                windowScene.windows.forEach { window in
                    window.overrideUserInterfaceStyle = newValue ? .dark : .light
                }
            }
        }
    }
}

struct AboutView: View {
    var body: some View {
        Text("About")
    }
}

struct SettingsView_Previews: PreviewProvider {
    static var previews: some View {
        SettingsView()
    }
}
