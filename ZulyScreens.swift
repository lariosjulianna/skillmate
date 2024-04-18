import UIKit
import SwiftUI
import Foundation

class TextViewController: UIViewController {
    
    let codeLength = 6
    var codeInputs = [UITextField]()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Set up the text label
        let textLabel = UILabel()
        textLabel.translatesAutoresizingMaskIntoConstraints = false
        textLabel.text = "My Code is"
        textLabel.textAlignment = .left
        textLabel.font = UIFont.systemFont(ofSize: 35)
        view.addSubview(textLabel)
        
        // Set up constraints for the text label
        NSLayoutConstraint.activate([
            textLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 20),
            textLabel.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 20)
        ])
        
        // Set up text fields for code input
        var previousTextField: UITextField?
        for _ in 0..<codeLength {
            let textField = UITextField()
            textField.translatesAutoresizingMaskIntoConstraints = false
            textField.placeholder = "-"
            textField.textAlignment = .center
            textField.font = UIFont.systemFont(ofSize: 25)
            textField.borderStyle = .roundedRect
            textField.keyboardType = .numberPad
            textField.delegate = self
            view.addSubview(textField)
            
            // Set up constraints for the text fields
            NSLayoutConstraint.activate([
                textField.heightAnchor.constraint(equalToConstant: 40),
                textField.widthAnchor.constraint(equalToConstant: 40),
            ])
            
            if let previousTextField = previousTextField {
                NSLayoutConstraint.activate([
                    textField.leadingAnchor.constraint(equalTo: previousTextField.trailingAnchor, constant: 10),
                    textField.centerYAnchor.constraint(equalTo: previousTextField.centerYAnchor)
                ])
            } else {
                NSLayoutConstraint.activate([
                    textField.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 20),
                    textField.centerYAnchor.constraint(equalTo: textLabel.bottomAnchor, constant: 30)
                ])
            }
            
            previousTextField = textField
            codeInputs.append(textField)
        }
        
        // Set up the continue button
        let continueButton = UIButton(type: .system)
        continueButton.translatesAutoresizingMaskIntoConstraints = false
        continueButton.setTitle("Continue", for: .normal)
        continueButton.titleLabel?.font = UIFont.systemFont(ofSize: 20)
        continueButton.addTarget(self, action: #selector(continueButtonTapped), for: .touchUpInside)
        view.addSubview(continueButton)
        
        // Set up constraints for the continue button
        NSLayoutConstraint.activate([
            continueButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            continueButton.topAnchor.constraint(equalTo: previousTextField!.bottomAnchor, constant: 30)
        ])
    }
    
    @objc func continueButtonTapped() {
        let firstNameViewController = FirstNameViewController()
        navigationController?.pushViewController(firstNameViewController, animated: true)
    }
}

extension TextViewController: UITextFieldDelegate {
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        let maxLength = 1
        let currentLength = textField.text?.count ?? 0
        guard currentLength < maxLength || string.isEmpty else { return false }
        return true
    }
}


class FirstNameViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Set up the text label for first name
        let textLabel = UILabel()
        textLabel.translatesAutoresizingMaskIntoConstraints = false
        textLabel.text = "My first name is"
        textLabel.textAlignment = .left
        textLabel.font = UIFont.systemFont(ofSize: 35)
        view.addSubview(textLabel)
        
        // Set up constraints for the text label
        NSLayoutConstraint.activate([
            textLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 20),
            textLabel.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 20)
        ])
        
        // Set up text field for entering first name
        let textField = UITextField()
        textField.translatesAutoresizingMaskIntoConstraints = false
        textField.placeholder = "Enter your first name"
        textField.textAlignment = .left
        textField.font = UIFont.systemFont(ofSize: 20)
        textField.borderStyle = .none
        view.addSubview(textField)
        
        // Set up constraints for the text field
        NSLayoutConstraint.activate([
            textField.topAnchor.constraint(equalTo: textLabel.bottomAnchor, constant: 20),
            textField.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 20),
            textField.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor, constant: -20),
            textField.heightAnchor.constraint(equalToConstant: 40)
        ])
        
        // Add a line underneath the text field
        let lineView = UIView()
        lineView.translatesAutoresizingMaskIntoConstraints = false
        lineView.backgroundColor = .gray
        view.addSubview(lineView)
        
        // Set up constraints for the line view
        NSLayoutConstraint.activate([
            lineView.topAnchor.constraint(equalTo: textField.bottomAnchor, constant: 1),
            lineView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 20),
            lineView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor, constant: -20),
            lineView.heightAnchor.constraint(equalToConstant: 1)
        ])
        
        // Set up the label for description
        let descriptionLabel = UILabel()
        descriptionLabel.translatesAutoresizingMaskIntoConstraints = false
        descriptionLabel.text = "This is how it will appear in skillmate. You will not be able to change it."
        descriptionLabel.textAlignment = .left
        descriptionLabel.font = UIFont.systemFont(ofSize: 10.5)
        descriptionLabel.textColor = .gray
        view.addSubview(descriptionLabel)
        
        // Set up constraints for the description label
        NSLayoutConstraint.activate([
            descriptionLabel.topAnchor.constraint(equalTo: lineView.bottomAnchor, constant: 10),
            descriptionLabel.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 20),
            descriptionLabel.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor, constant: -20)
        ])
        
        // Set up the continue button
        let continueButton = UIButton(type: .system)
        continueButton.translatesAutoresizingMaskIntoConstraints = false
        continueButton.setTitle("Continue", for: .normal)
        continueButton.titleLabel?.font = UIFont.systemFont(ofSize: 20)
        continueButton.addTarget(self, action: #selector(continueButtonTapped), for: .touchUpInside)
        view.addSubview(continueButton)
        
        // Set up constraints for the continue button
        NSLayoutConstraint.activate([
            continueButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            continueButton.topAnchor.constraint(equalTo: descriptionLabel.bottomAnchor, constant: 30)
        ])
        
        view.backgroundColor = .white
    }
    
    @objc func continueButtonTapped() {
        let birthdayViewController = BirthdayViewController()
        navigationController?.pushViewController(birthdayViewController, animated: true)
    }
}


class BirthdayViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Set up the text label for birthday
        let textLabel = UILabel()
        textLabel.translatesAutoresizingMaskIntoConstraints = false
        textLabel.text = "My birthday is"
        textLabel.textAlignment = .left
        textLabel.font = UIFont.systemFont(ofSize: 35)
        view.addSubview(textLabel)
        
        // Set up constraints for the text label
        NSLayoutConstraint.activate([
            textLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 20),
            textLabel.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 20)
        ])
        
        // Set up text field for entering birthday
        let textField = UITextField()
        textField.translatesAutoresizingMaskIntoConstraints = false
        textField.placeholder = "YYYY/MM/DD"
        textField.textAlignment = .left
        textField.font = UIFont.systemFont(ofSize: 20)
        textField.borderStyle = .none
        view.addSubview(textField)
        
        // Set up constraints for the text field
        NSLayoutConstraint.activate([
            textField.topAnchor.constraint(equalTo: textLabel.bottomAnchor, constant: 20),
            textField.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 20),
            textField.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor, constant: -20),
            textField.heightAnchor.constraint(equalToConstant: 40)
        ])
        
        // Add a line underneath the text field
        let lineView = UIView()
        lineView.translatesAutoresizingMaskIntoConstraints = false
        lineView.backgroundColor = .gray
        view.addSubview(lineView)
        
        // Set up constraints for the line view
        NSLayoutConstraint.activate([
            lineView.topAnchor.constraint(equalTo: textField.bottomAnchor, constant: 1),
            lineView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 20),
            lineView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor, constant: -20),
            lineView.heightAnchor.constraint(equalToConstant: 1)
        ])
        
        // Set up the label for description
        let descriptionLabel = UILabel()
        descriptionLabel.translatesAutoresizingMaskIntoConstraints = false
        descriptionLabel.text = "Your age will be public"
        descriptionLabel.textAlignment = .left
        descriptionLabel.font = UIFont.systemFont(ofSize: 12)
        descriptionLabel.textColor = .gray
        view.addSubview(descriptionLabel)
        
        // Set up constraints for the description label
        NSLayoutConstraint.activate([
            descriptionLabel.topAnchor.constraint(equalTo: lineView.bottomAnchor, constant: 10),
            descriptionLabel.leadingAnchor.constraint(equalTo: textField.leadingAnchor),
            descriptionLabel.trailingAnchor.constraint(equalTo: textField.trailingAnchor)
        ])
        
        // Set up the continue button
        let continueButton = UIButton(type: .system)
        continueButton.translatesAutoresizingMaskIntoConstraints = false
        continueButton.setTitle("Continue", for: .normal)
        continueButton.titleLabel?.font = UIFont.systemFont(ofSize: 20)
        continueButton.addTarget(self, action: #selector(continueButtonTapped), for: .touchUpInside)
        view.addSubview(continueButton)
        
        // Set up constraints for the continue button
        NSLayoutConstraint.activate([
            continueButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            continueButton.topAnchor.constraint(equalTo: descriptionLabel.bottomAnchor, constant: 30)
        ])
        
        view.backgroundColor = .white
    }
    
    @objc func continueButtonTapped() {
        let genderselectionViewController = GenderSelectionViewController()
        navigationController?.pushViewController(genderselectionViewController, animated: true)
    }
}

class GenderSelectionViewController: UIViewController {
    
    // Declare properties for buttons
    var womanButton: UIButton!
    var manButton: UIButton!
    var checkbox: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Set up the text label for gender selection
        let textLabel = UILabel()
        textLabel.translatesAutoresizingMaskIntoConstraints = false
        textLabel.text = "I am a"
        textLabel.textAlignment = .left
        textLabel.font = UIFont.systemFont(ofSize: 35)
        view.addSubview(textLabel)
        
        // Set up constraints for the text label
        NSLayoutConstraint.activate([
            textLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 20),
            textLabel.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 20)
        ])
        
        // Set up button for selecting gender "Woman"
        womanButton = UIButton(type: .system)
        womanButton.translatesAutoresizingMaskIntoConstraints = false
        womanButton.setTitle("Woman", for: .normal)
        womanButton.titleLabel?.font = UIFont.systemFont(ofSize: 20)
        womanButton.addTarget(self, action: #selector(womanButtonTapped), for: .touchUpInside)
        womanButton.layer.cornerRadius = 25 // Set corner radius to make it circular
        womanButton.layer.borderWidth = 2 // Add border
        womanButton.layer.borderColor = UIColor.black.cgColor // Border color
        view.addSubview(womanButton)
        
        // Set up constraints for the woman button
        NSLayoutConstraint.activate([
            womanButton.topAnchor.constraint(equalTo: textLabel.bottomAnchor, constant: 20),
            womanButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            womanButton.widthAnchor.constraint(equalToConstant: 200), // Set width
            womanButton.heightAnchor.constraint(equalToConstant: 50) // Set height
        ])
        
        // Set up button for selecting gender "Man"
        manButton = UIButton(type: .system)
        manButton.translatesAutoresizingMaskIntoConstraints = false
        manButton.setTitle("Man", for: .normal)
        manButton.titleLabel?.font = UIFont.systemFont(ofSize: 20)
        manButton.addTarget(self, action: #selector(manButtonTapped), for: .touchUpInside)
        manButton.layer.cornerRadius = 25 // Set corner radius to make it circular
        manButton.layer.borderWidth = 2 // Add border
        manButton.layer.borderColor = UIColor.black.cgColor // Border color
        view.addSubview(manButton)
        
        // Set up constraints for the man button
        NSLayoutConstraint.activate([
            manButton.topAnchor.constraint(equalTo: womanButton.bottomAnchor, constant: 20),
            manButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            manButton.widthAnchor.constraint(equalToConstant: 200), // Set width
            manButton.heightAnchor.constraint(equalToConstant: 50) // Set height
        ])
        
        // Set up checkbox for "Show my gender on my profile"
        checkbox = UIButton(type: .system)
        checkbox.translatesAutoresizingMaskIntoConstraints = false
        checkbox.setImage(UIImage(systemName: "square"), for: .normal)
        checkbox.tintColor = .black
        checkbox.addTarget(self, action: #selector(checkboxTapped), for: .touchUpInside)
        view.addSubview(checkbox)
        
        // Set up constraints for the checkbox
        NSLayoutConstraint.activate([
            checkbox.topAnchor.constraint(equalTo: manButton.bottomAnchor, constant: 20),
            checkbox.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor, constant: 20),
            checkbox.widthAnchor.constraint(equalToConstant: 25),
            checkbox.heightAnchor.constraint(equalToConstant: 25)
        ])
        
        // Set up label for "Show my gender on my profile"
        let showGenderLabel = UILabel()
        showGenderLabel.translatesAutoresizingMaskIntoConstraints = false
        showGenderLabel.text = "Show my gender on my profile"
        showGenderLabel.font = UIFont.systemFont(ofSize: 18)
        view.addSubview(showGenderLabel)
        
        // Set up constraints for the label
        NSLayoutConstraint.activate([
            showGenderLabel.centerYAnchor.constraint(equalTo: checkbox.centerYAnchor),
            showGenderLabel.leadingAnchor.constraint(equalTo: checkbox.trailingAnchor, constant: 10)
        ])
        
        // Set up the continue button
        let continueButton = UIButton(type: .system)
        continueButton.translatesAutoresizingMaskIntoConstraints = false
        continueButton.setTitle("Continue", for: .normal)
        continueButton.titleLabel?.font = UIFont.systemFont(ofSize: 20)
        continueButton.addTarget(self, action: #selector(continueButtonTapped), for: .touchUpInside)
        view.addSubview(continueButton)
        
        // Set up constraints for the continue button
        NSLayoutConstraint.activate([
            continueButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            continueButton.topAnchor.constraint(equalTo: checkbox.bottomAnchor, constant: 30)
        ])
        
        view.backgroundColor = .white
    }
    
    @objc func womanButtonTapped() {
        // Invert the colors when button is tapped
        womanButton.backgroundColor = womanButton.isSelected ? .white : .black
        womanButton.setTitleColor(womanButton.isSelected ? .black : .white, for: .normal)
        womanButton.isSelected = !womanButton.isSelected
        
    }

    @objc func manButtonTapped() {
        // Invert the colors when button is tapped
        manButton.backgroundColor = manButton.isSelected ? .white : .black
        manButton.setTitleColor(manButton.isSelected ? .black : .white, for: .normal)
        manButton.isSelected = !manButton.isSelected
    }

    @objc func checkboxTapped() {
        // Toggle isSelected property
        checkbox.isSelected = !checkbox.isSelected
        
        // Set the image based on isSelected
        if checkbox.isSelected {
            checkbox.setImage(UIImage(systemName: "checkmark.square.fill"), for: .normal)
        } else {
            checkbox.setImage(UIImage(systemName: "square"), for: .normal) // Set outline image
        }
    }

    @objc func continueButtonTapped() {
        // Lead to next page here (insert destination)
    }
}
