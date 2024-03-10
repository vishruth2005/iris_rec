require 'uri'

password = 'Infinity@1'
encoded_password = URI.encode_www_form_component(password)

puts encoded_password
