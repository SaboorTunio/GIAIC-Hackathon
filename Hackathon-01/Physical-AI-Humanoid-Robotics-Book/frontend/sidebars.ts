import type {SidebarsConfig} from '@docusaurus/types';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'doc',
      id: 'intro',
      label: 'Home'
    },
    {
      type: 'category',
      label: 'Module 1: Foundations',
      collapsed: false,
      items: [
        {
          type: 'doc',
          id: 'module-1/chapter-1-python-intro',
          label: 'Chapter 1: Python Fundamentals'
        },
        {
          type: 'doc',
          id: 'module-1/chapter-2-simulation-basics',
          label: 'Chapter 2: Simulation Basics'
        },
        {
          type: 'doc',
          id: 'module-1/chapter-3-math-robotics',
          label: 'Chapter 3: Mathematics for Robotics'
        },
        {
          type: 'doc',
          id: 'module-1/chapter-4-tools-setup',
          label: 'Chapter 4: Tools & Setup'
        },
      ],
    },
    {
      type: 'category',
      label: 'Module 2: The Body',
      collapsed: false,
      items: [
        {
          type: 'doc',
          id: 'module-2/chapter-5-sensors-overview',
          label: 'Chapter 5: Sensors'
        },
        {
          type: 'doc',
          id: 'module-2/chapter-6-actuators-control',
          label: 'Chapter 6: Actuators'
        },
        {
          type: 'doc',
          id: 'module-2/chapter-7-urdf-model',
          label: 'Chapter 7: URDF Models'
        },
        {
          type: 'doc',
          id: 'module-2/chapter-8-kinematics',
          label: 'Chapter 8: Kinematics'
        },
      ],
    },
    {
      type: 'category',
      label: 'Module 3: The Brain',
      collapsed: false,
      items: [
        {
          type: 'doc',
          id: 'module-3/chapter-9-computer-vision',
          label: 'Chapter 9: Computer Vision'
        },
        {
          type: 'doc',
          id: 'module-3/chapter-10-pytorch-basics',
          label: 'Chapter 10: PyTorch Basics'
        },
        {
          type: 'doc',
          id: 'module-3/chapter-11-reinforcement-learning',
          label: 'Chapter 11: Reinforcement Learning'
        },
        {
          type: 'doc',
          id: 'module-3/chapter-12-neural-networks',
          label: 'Chapter 12: Neural Networks'
        },
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Humanoid Control',
      collapsed: false,
      items: [
        {
          type: 'doc',
          id: 'module-4/chapter-13-walking-locomotion',
          label: 'Chapter 13: Walking & Locomotion'
        },
        {
          type: 'doc',
          id: 'module-4/chapter-14-grasping-manipulation',
          label: 'Chapter 14: Grasping & Manipulation'
        },
        {
          type: 'doc',
          id: 'module-4/chapter-15-agentic-behaviors',
          label: 'Chapter 15: Agentic Behaviors'
        },
        {
          type: 'doc',
          id: 'module-4/chapter-16-integration-project',
          label: 'Chapter 16: Integration Project'
        },
      ],
    },
  ],
};

export default sidebars;
