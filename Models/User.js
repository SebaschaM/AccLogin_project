const mongoose = require('mongoose');

mongoose.connect('mongodb+srv://schaquila:sebas123@cluster0.saeuaek.mongodb.net/myDatabase?retryWrites=true&w=majority', {
  useNewUrlParser: true,
  useCreateIndex: true,
  useUnifiedTopology: true
}).then(() => {
  console.log('Conexión a la base: Hecho');
}).catch((err) => {
  console.error('Conexión a la base Error: ', err);
});

const userSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
    trim: true,
  },
  password: {
    type: String,
    required: true,
    trim: true,
  },
  name: {
    type: String,
    required: true,
    trim: true,
  },
});

const User = mongoose.model('User', userSchema);

module.exports = User;