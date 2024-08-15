# curl_commands.sh

# Add data to generated_data table
curl -X POST "http://localhost:8000/api/generated_data/insert" \
     -H "Content-Type: application/json" \
     -d '{
       "code_mix_input": "example code-mixed input",
       "pure_sinhala_output": "example pure Sinhala output",
       "is_valid": "yes",
       "comment": "example comment",
       "updated_by": "test_user"
     }'

# Fetch data from generated_data table
curl -X GET "http://localhost:8000/generated_data/fetch" -H "Content-Type: application/json"
