const nodemailer = require("nodemailer");
const sendGmail = async (gmailId, errorMessage) => {
  const mailSettings = {
    service: "gmail",
    auth: {
      user: process.env.Gmail,
      pass: process.env.GmailPassword,
    },
  };
  const transporter = nodemailer.createTransport(mailSettings);
  try {
    await transporter.sendMail({
      from: mailSettings.auth.user,
      to: gmailId,
      subject: "An error was occured",
      html: `<!DOCTYPE html>
      <html>
      <head>
       </head>
       <body>
       <p>Error Message : ${errorMessage}</p>
      </body>
      </html>`,
    });
  } catch (error) {
    throw new Error(error.message);
  }
};

module.exports = sendGmail;
