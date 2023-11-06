STYLES = """

.gradio-container {
    background: linear-gradient(to top, #12100E  0%, #2B4162 100%) !important;
}

footer {visibility: hidden}


footer::after {
    content: "brought by Reza Amini | magnumical.ca";
    visibility: visible;
    font-size: 14px;
    color: white;
    position: absolute;
    bottom: 10px;
    left: 50%;
    transform: translateX(-50%); /* centering the text */
    cursor: pointer; /* Makes it appear clickable */
    text-decoration: none; /* No underline by default */
}

footer::after:hover {
    text-decoration: underline; /* Adding underline on hover */
}

/* Button Styling */
button {
    background-color: #FFD700 !important; /* Gold color */
    border: none;
    color: white; /* Text color */
    padding: 10px 20px; /* Button size */
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 12px; /* Rounded corners */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08); /* Shadow for depth */
}

button:hover {
    background-color: #e6b800 !important; /* Slightly darker gold on hover */
}

/* Input & Output Box Styling */
.interface-box {
    border: 1.5px dashed #FFD700 !important; /* Gold border */
    padding: 20px;
    border-radius: 8px; /* Rounded corners */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08); /* Shadow for depth */
}

/* Description Styling */
.description {
    font-size: 26px;  /* Adjust as per your requirement */
}

/* Label Styling */
label {
    font-size: 18px;  /* Bigger font size for labels */
    color: #333;     /* Dark color for label text */
}

/* Placeholder Styling */
input::placeholder {
    font-style: italic;  /* Italicized placeholder text */
}

"""