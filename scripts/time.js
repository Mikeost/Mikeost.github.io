function updateTime() {
   const timeBlock = document.getElementById("time");
   const date = new Date();
   const formatNumber = (num) => (num < 10 ? "0" + num : num);

   const formattedDate = `${formatNumber(date.getDate())}.${formatNumber(date.getMonth() + 1)}.${date.getFullYear()}`;
   const formattedTime = `${formatNumber(date.getHours())}:${formatNumber(date.getMinutes())}:${formatNumber(date.getSeconds())}`;

   timeBlock.innerHTML = `${formattedDate} ${formattedTime}`;
}

updateTime();
setInterval(updateTime, 500);