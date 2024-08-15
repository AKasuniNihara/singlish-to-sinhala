## API Endpoints

### Add Data to Generated Data

To add data to the `generated_data` table, use the following cURL command:

```bash
curl -X POST "http://localhost:8000/api/generated_data" \
     -H "Content-Type: application/json" \
     -d '{
       "code_mix_input": "example code-mixed input",
       "pure_sinhala_output": "example pure Sinhala output",
       "is_valid": "yes",
       "comment": "example comment",
       "updated_by": "test_user"
     }'
