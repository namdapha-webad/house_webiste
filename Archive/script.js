// Uncheck radio buttons (unfortunately this cannot be done with CSS alone)
document.querySelectorAll('input[type="radio"]').forEach(radio => {
    radio.addEventListener('click', (e) => {
        e.preventDefault();
        // Setting a timeout enables this hack to work
        setTimeout(() => radio.checked = !radio.checked, 0);
    });
});

// Map of avatar IDs to specific background image URLs
const avatarBackgrounds = {
    "avatar-1": "https://i.ytimg.com/vi/n9GGtkGvwj4/maxresdefault.jpg",
    "avatar-2": "https://external-preview.redd.it/aerial-view-of-bengaluru-city-v0-7jzTIh9e8U5CmUGSIv2AR8xwJmoUaVyglBW_efgZR9w.png?format=pjpg&auto=webp&s=707895414fb03400a174cccdb9658d313c2324c5",
    "avatar-3": "https://vj-prod-website-cms.s3.ap-southeast-1.amazonaws.com/1765681589chennai-1696645169332.jpg",
    "avatar-4": "https://vj-prod-website-cms.s3.ap-southeast-1.amazonaws.com/1765681589chennai-1696645169332.jpg",
    "avatar-5": "https://static2.tripoto.com/media/transfer/img/1891611/TripDocument/1620754416_chandigarh.gif",
    "avatar-6": "https://png.pngtree.com/thumb_back/fw800/background/20231003/pngtree-a-3d-render-illustration-of-the-all-india-war-memorial-commonly-image_13566303.png",
    "avatar-7": "https://content.r9cdn.net/rimg/dimg/f9/e4/73b8e1bc-lm-50366-16079f9e8be.jpg?crop=true&width=1020&height=498",
    "avatar-8": "https://thelucknowtribune.org/wp-content/uploads/2024/07/l32220211210173103.webp",
    "avatar-9": "https://cazloyd.com/wp-content/uploads/2023/09/How-Best-To-Spend-48-Hours-In-Kolkata-India.jpeg.webp",
    "avatar-10": "https://i.ytimg.com/vi/zBvT299ihHY/maxresdefault.jpg"
};

// Function to change background image with transparency
function changeBackgroundImage(event) {
    const avatarId = event.currentTarget.id; // Get the ID of the clicked avatar
    const backgroundUrl = avatarBackgrounds[avatarId]; // Get the corresponding background URL
    if (backgroundUrl) {
        document.body.style.transition = "background-image 1s ease";
        document.body.style.backgroundImage = `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(${backgroundUrl})`;
    }
}

// Add event listener to each avatar
document.querySelectorAll(".avatar").forEach(avatar => {
    avatar.addEventListener("click", changeBackgroundImage);
});
