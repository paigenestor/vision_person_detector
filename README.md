# Module vision_person_detector 

We would like you to create a custom sensor which will call a vision service and return true if an object is detected or false if no object is detected.
This will depend on the service created above with a single field called “person_detected” and it is set to 1 if our detection has a person and 0 if no person is detected.

## Model paige-nestor:vision_person_detector:person_detector

person_detected = 1 means a person was detected with a conifdence >0.6 by the Vision service
person_detected = 0 means a person was not detected or a person was detected with a conifdence <0.6 by the Vision service

### Configuration
The following attribute template can be used to configure this model:

```json
{
"attribute_1": <float>,
"attribute_2": <string>
}
```

#### Attributes

The following attributes are available for this model:

| Name          | Type   | Inclusion | Description                |
|---------------|--------|-----------|----------------------------|
| `attribute_1` | float  | Required  | Description of attribute 1 |
| `attribute_2` | string | Optional  | Description of attribute 2 |

#### Example Configuration

```json
{
  "attribute_1": 1.0,
  "attribute_2": "foo"
}
```

### DoCommand

If your model implements DoCommand, provide an example payload of each command that is supported and the arguments that can be used. If your model does not implement DoCommand, remove this section.

#### Example DoCommand

```json
{
  "command_name": {
    "arg1": "foo",
    "arg2": 1
  }
}
```
