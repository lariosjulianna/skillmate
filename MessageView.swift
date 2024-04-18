//
//  MessageView.swift
//  Group4Skillmate
//
//  Created by Dylan Calderon on 4/15/24.
//

import SwiftUI
import UIKit

struct Message: Identifiable {
    let id = UUID()
    let senderName: String
    let message: String
    let isCurrentUser: Bool // Indicates whether the message is sent by the current user
}

struct MessagesView: View {
    @State private var messages: [Message] = [
        Message(senderName: "Alice", message: "Hey!", isCurrentUser: false),
        Message(senderName: "You", message: "Hi Alice! How are you?", isCurrentUser: true),
        Message(senderName: "Alice", message: "I'm good, thanks! How about you?", isCurrentUser: false),
        // Add more sample messages as needed
    ]
    @State private var newMessageText = ""
    @State private var selectedImage: Image? = nil // Placeholder for selected image
    
    var body: some View {
        VStack(spacing: 0) {
            HStack {
                Spacer()
                
                Image(systemName: "person.circle")
                    .resizable()
                    .aspectRatio(contentMode: .fill)
                    .frame(width: 40, height: 40)
                    .clipShape(Circle())
                    .padding(.trailing, 8)
                
                Text("Alice") // Replace with the name of the person you are texting
                    .font(.headline)
                    .padding(.trailing, 8)
                
                Spacer()
            }
            .padding(.horizontal)
            
            Divider()
                .padding(.horizontal)
                .padding(.bottom, 8)
            
            ScrollView {
                LazyVStack(alignment: .leading, spacing: 8) {
                    ForEach(messages) { message in
                        MessageRow(message: message)
                            .padding(.horizontal)
                    }
                }
            }
            .padding(.vertical)
            .background(Color.white.opacity(0.1)) // Gray background for Messages section
            
            HStack {
                TextField("Type a message ...", text: $newMessageText)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    .padding(.horizontal)
                
                Button(action: sendMessage) {
                    Image(systemName: "arrow.up.circle.fill")
                        .resizable()
                        .frame(width: 30, height: 30)
                }
                .padding(.trailing)
            }
            .padding(.bottom)
            
            HStack {
                Spacer()
                
                // Clickable photo to open file picker
                Image("FileUpload") // Using the asset named "file upload"
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(width: 60, height: 60)
                    .onTapGesture {
                        openDocumentPicker()
                    }
                    .background()
            }
            .padding(.horizontal, 100)
            .padding(.bottom, -10)
        }
        .background(Color.white) // Background color for the entire view
        .navigationBarTitle("Messages", displayMode: .inline)
    }
    
    func sendMessage() {
        // Append the new message to the messages array
        messages.append(Message(senderName: "You", message: newMessageText, isCurrentUser: true))
        // Clear the text field after sending message
        newMessageText = ""
    }
    
    func openDocumentPicker() {
        let documentPicker = UIDocumentPickerViewController(documentTypes: ["public.data"], in: .import)
        documentPicker.delegate = Coordinator()
        UIApplication.shared.windows.first?.rootViewController?.present(documentPicker, animated: true, completion: nil)
    }
}

struct MessageRow: View {
    let message: Message
    
    var body: some View {
        HStack {
            if !message.isCurrentUser {
                Image(systemName: "person.circle")
                    .resizable()
                    .aspectRatio(contentMode: .fill)
                    .frame(width: 40, height: 40)
                    .clipShape(Circle())
                    .padding(.trailing, 8)
            }
            
            Text(message.message)
                .padding(12)
                .foregroundColor(.white)
                .background(message.isCurrentUser ? Color.blue : Color.gray)
                .cornerRadius(15)
                .overlay(
                    RoundedRectangle(cornerRadius: 15)
                        .stroke(message.isCurrentUser ? Color.blue : Color.gray, lineWidth: 1)
                )
            
            if message.isCurrentUser {
                Spacer(minLength: 0) // Pushes message to right
            } else {
                Spacer() // Pushes message to left
            }
        }
    }
}

struct MessagesView_Previews: PreviewProvider {
    static var previews: some View {
        MessagesView()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

// Coordinator to handle the delegate methods of UIDocumentPickerViewController
class Coordinator: NSObject, UIDocumentPickerDelegate {
    func documentPicker(_ controller: UIDocumentPickerViewController, didPickDocumentsAt urls: [URL]) {
        // Handle the picked documents here
        print("Picked documents: \(urls)")
    }
    
    func documentPickerWasCancelled(_ controller: UIDocumentPickerViewController) {
        // Handle cancellation
        print("Document picker was cancelled")
    }
}
