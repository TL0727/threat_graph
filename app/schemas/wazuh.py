from pydantic import BaseModel, Field, field_validator
from typing import List, Dict, Optional, Tuple
from datetime import datetime

class Agent(BaseModel):
    agent_name: str = Field(..., example="test-agent-1", description="Name of the agent")
    agent_id: str = Field(..., example="001", description="Unique identifier of the agent")
    ip: str = Field(..., example="192.168.1.100", description="IP address of the agent")
    agent_status: str = Field(..., example="Active", description="Current status of the agent")
    status_code: int = Field(..., example=0, description="Status code of the agent")
    last_keep_alive: datetime = Field(..., example="2023-07-30T12:00:00Z", description="Last keep alive timestamp")
    os: str = Field(..., example="Ubuntu", description="Operating system of the agent")
    os_version: str = Field(..., example="20.04", description="Version of the operating system")
    group_name: str = Field(..., example="group1", description="Name of the group this agent belongs to")
    wazuh_data_type: str = Field(default="agent_info", Literal=True, description="Type of Wazuh data")

class WazuhEvent(BaseModel):
    timestamp: datetime = Field(..., example="2023-07-30T12:05:00Z", description="Timestamp of the event")
    agent_id: str = Field(..., example="001", description="ID of the agent that generated the event")
    agent_ip: str = Field(..., example="192.168.1.100", description="IP of the agent that generated the event")
    rule_description: str = Field(..., example="File added to the system.", description="Description of the rule that triggered")
    rule_level: int = Field(..., example=3, description="Level of the rule that triggered")
    rule_id: str = Field(..., example="550", description="ID of the rule that triggered")
    rule_mitre_id: Optional[str] = Field(None, example="T1078", description="MITRE ATT&CK technique ID")
    rule_mitre_tactic: Optional[str] = Field(None, example="Persistence", description="MITRE ATT&CK tactic")
    rule_mitre_technique: Optional[str] = Field(None, example="Valid Accounts", description="MITRE ATT&CK technique")
    group_name: str = Field(..., example="group1", description="Name of the group this event belongs to")
    wazuh_data_type: str = Field(default="wazuh_events", Literal=True, description="Type of Wazuh data")

class AgentInfoRequest(BaseModel):
    agent: List[Agent]
    events: List[WazuhEvent]

    class Config:
        schema_extra = {
            "example": {
                "agent": [  # Changed from 'agents' to 'agent'
                    {
                        "agent_name": "Agent_001",
                        "agent_id": "001",
                        "ip": "192.168.1.101",
                        "agent_status": "active",
                        "status_code": 0,
                        "last_keep_alive": "2024-08-02T10:30:00Z",
                        "group_name": "threathunting",
                        "os": "Ubuntu",
                        "os_version": "20.04",
                        "wazuh_data_type": "agent_info"
                    },
                    {
                        "agent_name": "Agent_002",
                        "agent_id": "002",
                        "ip": "192.168.1.102",
                        "agent_status": "active",
                        "status_code": 0,
                        "last_keep_alive": "2024-08-02T10:35:00Z",
                        "group_name": "networksecurity",
                        "os": "Windows",
                        "os_version": "10",
                        "wazuh_data_type": "agent_info"
                    },
                    {
                        "agent_name": "Agent_003",
                        "agent_id": "003",
                        "ip": "192.168.1.103",
                        "agent_status": "disconnected",
                        "status_code": 1,
                        "last_keep_alive": "2024-08-02T09:45:00Z",
                        "group_name": "threathunting",
                        "os": "CentOS",
                        "os_version": "8",
                        "wazuh_data_type": "agent_info"
                    }
                ],
                "events": [
                    {
                        "timestamp": "2024-08-02T11:00:00Z",
                        "agent_id": "001",
                        "agent_ip": "192.168.1.101",
                        "rule_description": "File integrity checksum changed.",
                        "rule_level": 7,
                        "rule_id": "550",
                        "rule_mitre_id": "T1565",
                        "rule_mitre_tactic": ["Impact"],
                        "rule_mitre_technique": "Data Manipulation",
                        "group_name": "threathunting",
                        "wazuh_data_type": "wazuh_events"
                    },
                    {
                        "timestamp": "2024-08-02T11:05:00Z",
                        "agent_id": "002",
                        "agent_ip": "192.168.1.102",
                        "rule_description": "Multiple authentication failures.",
                        "rule_level": 10,
                        "rule_id": "5710",
                        "rule_mitre_id": "T1110",
                        "rule_mitre_tactic": ["Credential Access"],
                        "rule_mitre_technique": "Brute Force",
                        "group_name": "networksecurity",
                        "wazuh_data_type": "wazuh_events"
                    },
                    {
                        "timestamp": "2024-08-02T11:10:00Z",
                        "agent_id": "003",
                        "agent_ip": "192.168.1.103",
                        "rule_description": "Possible SQL injection attempt.",
                        "rule_level": 15,
                        "rule_id": "31101",
                        "rule_mitre_id": "T1190",
                        "rule_mitre_tactic": ["Initial Access"],
                        "rule_mitre_technique": "Exploit Public-Facing Application",
                        "group_name": "threathunting",
                        "wazuh_data_type": "wazuh_events"
                    }
                ]
            }
        }

class AgentInfoResponse(BaseModel):
    message: str = Field(..., example="Agents info and events saved successfully", description="Response message")
    agent_ids: List[str] = Field(..., example=["001", "002"], description="IDs of the agents that were saved")
    events_saved: Dict[str, int] = Field(..., example={"001": 5, "002": 3}, description="Number of events saved for each agent")
    
class GetAgentInfoByTimeResponse(BaseModel):
    agent_info: Dict
    events: List[Dict]

    class Config:
        schema_extra = {
            "example": {
                "agent_info": {
                    "agent_name": "test-agent-1",
                    "agent_id": "001",
                    "ip": "192.168.1.100",
                    "agent_status": "Active",
                    "status_code": 0,
                    "last_keep_alive": "2023-07-30T12:00:00Z",
                    "os": "Ubuntu",
                    "os_version": "20.04",
                    "group_name": "group1",
                    "wazuh_data_type": "agent_info"
                },
                "events": [
                    {
                        "timestamp": "2023-07-30T12:05:00Z",
                        "agent_id": "001",
                        "agent_ip": "192.168.1.100",
                        "rule_description": "File added to the system.",
                        "rule_level": 3,
                        "rule_id": "550",
                        "rule_mitre_id": "T1078",
                        "rule_mitre_tactic": "Persistence",
                        "rule_mitre_technique": "Valid Accounts",
                        "group_name": "group1",
                        "wazuh_data_type": "wazuh_events"
                    }
                ]
            }
        }

class GetAgentInfoByGroupRequest(BaseModel):
    start_time: datetime = Field(..., example="2023-07-30T00:00:00Z", description="Start time for event query")
    end_time: datetime = Field(..., example="2023-07-31T00:00:00Z", description="End time for event query")

class GetAgentInfoByGroupResponse(BaseModel):
    agents: List[Dict]
    events: List[Dict]

    class Config:
        schema_extra = {
            "example": {
                "agents": [
                    {
                        "agent_name": "test-agent-1",
                        "agent_id": "001",
                        "ip": "192.168.1.100",
                        "agent_status": "Active",
                        "status_code": 0,
                        "last_keep_alive": "2023-07-30T12:00:00Z",
                        "os": "Ubuntu",
                        "os_version": "20.04",
                        "group_name": "group1",
                        "wazuh_data_type": "agent_info"
                    },
                    {
                        "agent_name": "test-agent-2",
                        "agent_id": "002",
                        "ip": "192.168.1.101",
                        "agent_status": "Active",
                        "status_code": 0,
                        "last_keep_alive": "2023-07-30T12:00:00Z",
                        "os": "CentOS",
                        "os_version": "7",
                        "group_name": "group1",
                        "wazuh_data_type": "agent_info"
                    }
                ],
                "events": [
                    {
                        "timestamp": "2023-07-30T12:05:00Z",
                        "agent_id": "001",
                        "agent_ip": "192.168.1.100",
                        "rule_description": "File added to the system.",
                        "rule_level": 3,
                        "rule_id": "550",
                        "rule_mitre_id": "T1078",
                        "rule_mitre_tactic": ["Persistence"],
                        "rule_mitre_technique": "Valid Accounts",
                        "group_name": "group1",
                        "wazuh_data_type": "wazuh_events"
                    },
                    {
                        "timestamp": "2023-07-30T12:10:00Z",
                        "agent_id": "002",
                        "agent_ip": "192.168.1.101",
                        "rule_description": "Network connection detected",
                        "rule_level": 2,
                        "rule_id": "5001",
                        "group_name": "group1",
                        "wazuh_data_type": "wazuh_events"
                    }
                ]
            }
        }

class AgentSummary(BaseModel):
    id: int = Field(..., example=1, description="Unique identifier for the summary item")
    agent_name: str = Field(..., example="Active agents", description="Name or category of the summary item")
    data: int = Field(..., example=20, description="Count or value for the summary item")

class AgentSummaryRequest(BaseModel):
    start_time: datetime = Field(..., description="Start time for the summary period")
    end_time: datetime = Field(..., description="End time for the summary period")

class AgentSummaryResponse(BaseModel):
    agents: List[AgentSummary]

    class Config:
        schema_extra = {
            "example": {
                "agents": [
                    {"id": 1, "agent_name": "Active agents", "data": 20},
                    {"id": 2, "agent_name": "Total agents", "data": 28},
                    {"id": 3, "agent_name": "Active Windows agents", "data": 15},
                    {"id": 4, "agent_name": "Windows agents", "data": 17},
                    {"id": 5, "agent_name": "Active Linux agents", "data": 5},
                    {"id": 6, "agent_name": "Linux agents", "data": 9},
                    {"id": 7, "agent_name": "Active MacOS agents", "data": 0},
                    {"id": 8, "agent_name": "MacOS agents", "data": 2}
                ]
            }
        }
        
class AgentMessage(BaseModel):
    id: int = Field(..., example=1)
    time: str = Field(..., example="Jul 30, 2024 @ 03:36:11.534")
    agent_id: str = Field(..., example="001")
    rule_description: str = Field(..., example="VirusTotal: Alert - c:\\users\\vm_user\\downloads\\annabelle.exe - 62 engines detected this file")
    rule_mitre_tactic: str = Field(None, example="Execution")
    rule_mitre_id: str = Field(None, example="T1203")
    rule_level: int = Field(..., ge=9, le=15, example=12, description="Rule level (9-15)")

class AgentMessagesResponse(BaseModel):
    total: int = Field(..., description="Total number of high-level messages in the specified time range")
    datas: List[AgentMessage] = Field(..., description="List of high-level messages")

    class Config:
        schema_extra = {
            "example": {
                "total": 100,
                "datas": [
                    {
                        "id": 1,
                        "time": "Jul 30, 2024 @ 03:36:11.534",
                        "agent_id": "001",
                        "rule_description": "VirusTotal: Alert - c:\\users\\vm_user\\downloads\\annabelle.exe - 62 engines detected this file",
                        "rule_mitre_tactic": "Execution",
                        "rule_mitre_id": "T1203",
                        "rule_level": 12
                    }
                ]
            }
        }

class AgentMessagesRequest(BaseModel):
    start_time: datetime = Field(..., description="Start time for the message query")
    end_time: datetime = Field(..., description="End time for the message query")
    limit: int = Field(20, ge=1, le=100, description="Maximum number of high-level messages to return")

class LineData(BaseModel):
    name: str = Field(..., description="Name of the data series")
    type: str = Field(default="line", description="Type of the chart (always 'line' for this endpoint)")
    data: List[Tuple[datetime, int]] = Field(..., description="List of data points (timestamp, value)")

    @field_validator('type')
    def validate_type(cls, v):
        if v != "line":
            raise ValueError("Type must be 'line'")
        return v

class LineChartResponse(BaseModel):
    label: List[str] = Field(..., description="List of labels for the data series")
    datas: List[LineData] = Field(..., description="List of data series for the chart")

class LineChartRequest(BaseModel):
    start_time: datetime = Field(..., description="Start time for the chart data")
    end_time: datetime = Field(..., description="End time for the chart data")
    
class TotalEventRequest(BaseModel):
    start_time: datetime = Field(..., description="Start time for the total event count")
    end_time: datetime = Field(..., description="End time for the total event count")

class TotalEventResponse(BaseModel):
    count: str = Field(..., description="Formatted count of total events with levels 8-14")

class TotalEventAPIResponse(BaseModel):
    success: bool = Field(..., description="Indicates if the request was successful")
    content: TotalEventResponse = Field(..., description="Contains the total event count data")
    
class PieChartItem(BaseModel):
    value: int = Field(..., description="Count or value for the pie chart slice")
    name: str = Field(..., description="Name or label for the pie chart slice")

class PieChartData(BaseModel):
    top_agents: List[PieChartItem] = Field(..., description="Top 5 agents")
    top_mitre: List[PieChartItem] = Field(..., description="Top MITRE ATT&CKs")
    top_events: List[PieChartItem] = Field(..., description="Top 5 Events")
    top_event_counts: List[PieChartItem] = Field(..., description="Top 5 Event Counts by Agent Name")

class PieChartRequest(BaseModel):
    start_time: datetime = Field(..., description="Start time for the pie chart data")
    end_time: datetime = Field(..., description="End time for the pie chart data")

class PieChartAPIResponse(BaseModel):
    success: bool = Field(..., description="Indicates if the request was successful")
    content: PieChartData = Field(..., description="Contains the pie chart data")