import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import { BASE_URL } from "../../../../../constants/urls";

const ArchieveProjectDetails = () => {
  const location = useLocation();
  const [teamMemberOptions, setTeamMemberOptions] = useState([]);
  const [teamLeaderOptions, setTeamLeaderOptions] = useState([]);
  const [techStackOptions, setTechStackOptions] = useState([]);
  const [stacks, setStacks] = useState();
  const [team, setTeam] = useState();
  const { project } = location.state || {};
  useEffect(() => {
    const fetchTeamMembers = async () => {
      const authToken = localStorage.getItem("BearerToken");
      try {
        const response = await fetch(`${BASE_URL}users/`, {
          method: "GET",
          headers: {
            Authorization: `Bearer ${authToken}`,
          },
        });
        const data = await response.json();
        const options = data.map((user) => ({
          value: user.id,
          label: user.username,
        }));
        setTeamMemberOptions(options);
        setTeamLeaderOptions(options);
      } catch (error) {
        console.error("Error fetching users:", error);
      }
    };

    fetchTeamMembers();
  }, []);

  useEffect(() => {
    const authToken = localStorage.getItem("BearerToken");
    const fetchTechStacks = async () => {
      try {
        const response = await fetch(`${BASE_URL}techstacks/`, {
          method: "GET",
          headers: {
            Authorization: `Bearer ${authToken}`,
          },
        });
        const data = await response.json();

        const options = data.map((stack) => ({
          value: stack.id,
          label: stack.name,
        }));

        setTechStackOptions(options);
      } catch (error) {
        console.error("Error fetching tech stacks:", error);
      }
    };

    fetchTechStacks();
  }, []);

  useEffect(() => {
    try {
      const tech_stack = techStackOptions
        .filter((option) => project.tech_stack.includes(option.value))
        .map((option) => option.label);
      setStacks(tech_stack);
      setTeam(
        teamLeaderOptions
          .filter((option) => project.development_team.includes(option.value))
          .map((option) => option.label)
      );

      project.responsible_person = teamMemberOptions.filter(
        (option) => option.value === project.responsible_person
      )[0];
    } catch {
      console.log("not edit");
    }
  }, [project, techStackOptions, teamMemberOptions]);

  return (
    <div className="page-wrapper">
      <div className="content container-fluid">
        <div className="row">
          <div className="col-md-12">
            <div className="card">
              <div className="card-body">
                <h4 className="payslip-title">Project Details</h4>
                <form className="project-details-form">
                  <div className="form-group">
                    <img
                      id="projectLogo"
                      src={project.logo_icon}
                      className="inv-logo"
                      alt="Logo"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="projectId">Project ID</label>
                    <input
                      type="text"
                      id="projectId"
                      value={project.id}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="startDate">Start Date</label>
                    <input
                      type="text"
                      id="startDate"
                      value={project.created_at}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="endDate">End Date</label>
                    <input
                      type="text"
                      id="endDate"
                      value={project.end_date}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="projectName">Project Name</label>
                    <input
                      type="text"
                      id="projectName"
                      value={project.name}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="projectDescription">
                      Project Description
                    </label>
                    <textarea
                      id="projectDescription"
                      value={project.description}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="clientName">Client Name</label>
                    <input
                      type="text"
                      id="clientName"
                      value={project.client_name}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="projectLeader">Project Lead</label>
                    <input
                      type="text"
                      id="projectLeader"
                      value={project.responsible_person}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="teamMembers">Team Members</label>
                    <textarea
                      id="teamMembers"
                      value={team}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="githubLink">Github Link</label>
                    <input
                      type="text"
                      id="githubLink"
                      value={project.git_link}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="figmaLink">Figma Link</label>
                    <input
                      type="text"
                      id="figmaLink"
                      value={project.figma_link}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="liveLink">Live Link</label>
                    <input
                      type="text"
                      id="liveLink"
                      value={project.live_link}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="serverEmail">Server Login Email</label>
                    <input
                      type="text"
                      id="serverEmail"
                      value={project.server_email}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="serverPassword">
                      Server Login Password
                    </label>
                    <input
                      type="text"
                      id="serverPassword"
                      value={project.server_password}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="industry">Industry</label>
                    <input
                      type="text"
                      id="industry"
                      value={project.industry}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="techStack">Tech Stack</label>
                    <input
                      type="text"
                      id="techStack"
                      value={stacks}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="platform">Platform</label>
                    <input
                      type="text"
                      id="platform"
                      value={project.platforms}
                      readOnly
                      className="form-control"
                    />
                  </div>
                  <br></br>

                  <div className="form-group">
                    <label htmlFor="documents">Documents</label>
                    <textarea
                      id="documents"
                      value={project.documents}
                      readOnly
                      className="form-control"
                    />
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ArchieveProjectDetails;
