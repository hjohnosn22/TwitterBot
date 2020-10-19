driver
main();  // Run the main function once first before running the interval ticks. This is optional.
setInterval(main, Math.floor(((Math.random() * 10) + 5) * 1000) * 60);