const ERROR_CODES = {
  'Unable to log in with provided credentials.': 'Неверная почта или пароль.',
  'This email already exists': 'Пользователь с такой электронной почтой уже зарегистрирован.',
  'This full name already exists': 'Пользователь с таким именем уже зарегистрирован.'
}

export function getErrorMessage (code) {
  code = Object.values(code)[0]
  return ERROR_CODES[code] ? ERROR_CODES[code] : 'Неизвестная ошибка'
}
