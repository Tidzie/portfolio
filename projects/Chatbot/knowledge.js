const gzuKnowledge = {
    "general": {
        "name": "Great Zimbabwe University",
        "location": "Masvingo, Zimbabwe",
        "established": "1999",
        "type": "Public University",
        "motto": "Knowledge, Innovation, Excellence"
    },
    "faculties": [
        "Faculty of Agriculture and Environmental Science",
        "Faculty of Arts",
        "Faculty of Commerce",
        "Faculty of Education",
        "Faculty of Law",
        "Faculty of Science and Technology",
        "Faculty of Social Sciences"
    ],
    "campuses": [
        "Main Campus (Masvingo)",
        "Harare Campus",
        "Zvishavane Campus"
    ],
    "programs": {
        "undergraduate": [
            "Bachelor of Agriculture",
            "Bachelor of Arts",
            "Bachelor of Commerce",
            "Bachelor of Education",
            "Bachelor of Laws",
            "Bachelor of Science",
            "Bachelor of Social Work"
        ],
        "postgraduate": [
            "Master of Business Administration",
            "Master of Science",
            "Master of Arts",
            "Doctor of Philosophy"
        ]
    },
    "contact": {
        "phone": "+263 39 226 8515",
        "email": "info@gzu.ac.zw",
        "website": "www.gzu.ac.zw"
    }
};

// Function to find relevant information based on user query
function findAnswer(query) {
    query = query.toLowerCase();
    
    // Check for general information
    if (query.includes("name") || query.includes("what is")) {
        return `Great Zimbabwe University (GZU) is a ${gzuKnowledge.general.type} located in ${gzuKnowledge.general.location}. It was established in ${gzuKnowledge.general.established}.`;
    }
    
    // Check for faculties
    if (query.includes("faculty") || query.includes("faculties") || query.includes("schools")) {
        return `GZU has the following faculties:\n${gzuKnowledge.faculties.join("\n")}`;
    }
    
    // Check for campuses
    if (query.includes("campus") || query.includes("location")) {
        return `GZU has three campuses:\n${gzuKnowledge.campuses.join("\n")}`;
    }
    
    // Check for programs
    if (query.includes("program") || query.includes("course") || query.includes("study")) {
        return `GZU offers various programs including:\nUndergraduate:\n${gzuKnowledge.programs.undergraduate.join("\n")}\n\nPostgraduate:\n${gzuKnowledge.programs.postgraduate.join("\n")}`;
    }
    
    // Check for contact information
    if (query.includes("contact") || query.includes("phone") || query.includes("email")) {
        return `You can contact GZU at:\nPhone: ${gzuKnowledge.contact.phone}\nEmail: ${gzuKnowledge.contact.email}\nWebsite: ${gzuKnowledge.contact.website}`;
    }
    
    // Default response
    return "I'm sorry, I don't have specific information about that. You can ask me about GZU's faculties, programs, campuses, or contact information.";
} 