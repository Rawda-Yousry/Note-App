# Front End

- **Text Box**: Allows the user to enter their first name.
- **Submit Button**: Submits the content of the text box.
  - **Validation**: Ensures the text box is not empty before submission.
- **Display Name**: The entered name appears on the HTML page using JavaScript.
- **Local Storage**: Saves a welcome message (`"Welcome back, [name]"`) so it appears when the user returns.
- **Note Text Box**: Allows the user to add a note.
- **Hyperlink**: Directs the user to a page where notes are viewed.
- **Search Text Box**: Allows the user to enter text to search within notes.
- **Search and View Notes**: Displays search results and notes on the same page.

# Back End

- **Add Note**: Sends the note to the server using a GET method.
  - **Function**: Handles and saves the note data.
- **View Notes**: Directs the user to a route where a function retrieves the notes.
- **Search Note**: Sends the search query to the server using a GET method.
  - **Function**: Handles the search and returns matching notes or a "Not Found" message.
